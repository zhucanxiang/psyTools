from pdf2image import convert_from_path
from PIL import Image
from paddleocr import PaddleOCR
import os
import re
from document_loader.baseLoader import BaseLoader


class Pdf2Img(BaseLoader):
    def __init__(self, file_path, output_file_path):
        self.file_path = file_path
        self.output_file_path = output_file_path
        self.file_dir = '/'.join(file_path.split("/")[:-1])
        self.img_file_dir = self.file_dir + "/imgs"
        self.region_file_dir = self.file_dir + "/region"
        if not os.path.exists(self.img_file_dir):
            os.makedirs(self.img_file_dir)
        if not os.path.exists(self.region_file_dir):
            os.makedirs(self.region_file_dir)

    def build(self) -> list:
        self.crop_img(self.pdf2img())
        self.image_ocr_txt(self.region_file_dir, self.output_file_path)

    def pdf2img(self) -> list:
        imgs = list()
        pages = convert_from_path(self.file_path)
        for i, page in enumerate(pages):
            page.save(f'{self.img_file_dir}/{i + 1}.jpg', 'JPEG')
            img = Image.open(f'{self.img_file_dir}/{i + 1}.jpg')
            imgs.append(img)
        return imgs

    def crop_img(self, imgs: list) -> list:
        for i, img in enumerate(imgs):
            width, height = img.size
            box1 = (0, 0, width / 2, height)
            box2 = (width / 2, 0, width, height)
            region_1 = img.crop(box1)
            region_2 = img.crop(box2)
            region_1.save(f'{self.region_file_dir}/{i*2+1}.jpg', 'JPEG')
            region_2.save(f'{self.region_file_dir}/{i*2+2}.jpg', 'JPEG')

    def image_ocr_txt(self, region_filedir, output_filepath):
        fout = open(output_filepath, 'w', encoding='utf-8')
        ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=False, show_log=False)
        filenames = os.listdir(region_filedir)
        # 使用正则表达式从文件名中提取数字序号
        pattern = re.compile(r'\d+')
        filenames_with_numbers = [(filename, int(pattern.search(filename).group())) for filename in filenames if
                                  pattern.search(filename)]
        # 按数字序号排序
        sorted_filenames_with_numbers = sorted(filenames_with_numbers, key=lambda x: x[1])

        # 打印排序后的文件名
        for filename, number in sorted_filenames_with_numbers:
            print('filename: ' + filename)
            file_path = os.path.join(region_filedir, filename)
            if os.path.isfile(file_path):
                result = ocr.ocr(img=file_path)
                ocr_result = [i[1][0] for line in result for i in line]
                fout.write(''.join(ocr_result) + '\n')
        fout.flush()
        fout.close()

    def parse_content(self, final_file_path):
        content = ''
        fout = open(final_file_path, 'w', encoding='utf-8')
        with open(self.output_file_path, 'r', encoding='utf-8') as fin:
            for line in fin.readlines():
                content += line.strip()
            cases = content.split('病例摘要')
            for case in cases:
                if '病例讨论' and '【本例诊断】' in case:
                    case_items = case.split('病例讨论')
                    if len(case_items) == 2:
                        case_summary = case_items[0]
                        case_discussion_diagnose= case_items[1]
                        case_others = case_discussion_diagnose.split('【本例诊断】')
                        if len(case_others) == 2:
                            case_discussion = case_others[0]
                            case_diagnose = case_others[1]
                            fout.write('\t'.join([case_summary, case_diagnose]) + '\n')
        fout.flush()
        fout.close()



loader = Pdf2Img("/Users/zhucanxiang/Desktop/psy_resources/psy_samples_7_240.pdf", "/Users/zhucanxiang/Desktop/psy_resources/psy_samples_7_240.txt")
loader.build()
#loader.parse_content("/Users/zhucanxiang/Desktop/psy_resources/psy_samples_7_240.struct.txt")
#loader.image_ocr_txt("/Users/zhucanxiang/Desktop/sample", "/Users/zhucanxiang/Desktop/sample.txt")