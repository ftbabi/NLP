#-*- coding ： utf-8 -*-

import json
import jieba
import random

def load(filename, parapath, savepath, half=3):
    question_para_dict = {}

    ques_id = 0
    first_ans = []
    with open(filename, 'r') as f:
        load_dict = json.load(f)
        for piece in load_dict:
            if piece[1]:
                # 有答案并且是标定的答案不是手输入的
                for i in range(2, len(piece)):
                    if not piece[i][0]:
                        continue
                    one = dict()
                    one['question'] = piece[i][1].strip('?')
                    one['question_type'] = 'ENTITY'
                    one['fact_or_opinion'] = 'FACT'
                    one['question_id'] = ques_id
                    one['segmented_question'] = list(jieba.cut(one['question']))
                    first_ans.append(one)
                    question_para_dict[ques_id] = int(piece[0])

                    ques_id += 1

    with open(parapath, 'r', encoding='utf-8') as f:
        load_dict = json.load(f)
        sentence = []
        seg_sentence = []
        for line in load_dict:
            sent = ''.join(line)
            sentence.append(sent)
            seg_sentence.append(line)

        for sample in first_ans:
            doc = []
            for i in range(5):
                doc_dict =dict()
                tar = question_para_dict[sample['question_id']]
                start = max(0, tar-half)
                end = min(len(sentence), tar+1+half)
                # one_seg = []
                # one_para = []
                insertit = random.randint(start, end+1)
                leftseg = []
                # left = []
                rightseg = []
                # right = []
                left = ""
                right = ""
                for i in range(start, end):
                    if i == tar:
                        continue
                    pointerseg = leftseg
                    pointer = left
                    if i >= insertit:
                        rightseg += seg_sentence[i]
                        right += sentence[i]
                        # pointerseg = rightseg
                        # pointer = right
                    else:
                        leftseg += seg_sentence[i]
                        left += sentence[i]
                    # pointerseg.append(seg_sentence[i])
                    # pointer.append(sentence[i])

                # one_seg = leftseg + [seg_sentence[tar]] + rightseg
                # one_para = left + [sentence[tar]] + right
                one_seg = leftseg + seg_sentence[tar] + rightseg
                one_para = left + sentence[tar] + right

                doc_dict['segmented_paragraphs'] = [one_seg]
                doc_dict['paragraphs'] = [one_para]
                doc.append(doc_dict)
            sample['documents'] = doc

    with open(savepath, 'w', encoding='utf-8') as f:
        for i in first_ans:
            f.write(json.dumps(i, ensure_ascii=False))
            f.write('\n')
        # f.write(json.dumps(first_ans, ensure_ascii=False))
        # json.dump(first_ans, f)

def load_word_level(filename, parapath, savepath, half=1):
    question_para_dict = {}

    ques_id = 0
    first_ans = []
    with open(filename, 'r') as f:
        load_dict = json.load(f)
        for piece in load_dict:
            if piece[1]:
                # 有答案并且是标定的答案不是手输入的
                for i in range(2, len(piece)):
                    if not piece[i][0]:
                        continue
                    one = dict()
                    one['question'] = piece[i][1].strip('?')
                    one['question_type'] = 'ENTITY'
                    one['fact_or_opinion'] = 'FACT'
                    one['question_id'] = ques_id
                    one['segmented_question'] = list(jieba.cut(one['question']))
                    first_ans.append(one)
                    question_para_dict[ques_id] = int(piece[0])

                    ques_id += 1

    with open(parapath, 'r', encoding='utf-8') as f:
        load_dict = json.load(f)
        sentence = []
        seg_sentence = []
        for line in load_dict:
            sent = ''.join(line)
            sentence.append(sent)
            seg_sentence.append(line)

        for sample in first_ans:
            doc = []
            for i in range(5):
                doc_dict =dict()
                tar = question_para_dict[sample['question_id']]
                start = max(0, tar-half)
                end = min(len(sentence), tar+1+half)
                # one_seg = []
                # one_para = []
                insertit = random.randint(start, end+1)
                leftseg = []
                left = []
                rightseg = []
                right = []
                for i in range(start, end):
                    if i == tar:
                        continue
                    pointerseg = leftseg
                    pointer = left
                    if i >= insertit:
                        pointerseg = rightseg
                        pointer = right
                    pointerseg.append(seg_sentence[i])
                    pointer.append(sentence[i])

                one_seg = leftseg + [seg_sentence[tar]] + rightseg
                one_para = left + [sentence[tar]] + right
                doc_dict['segmented_paragraphs'] = one_seg
                doc_dict['paragraphs'] = one_seg
                doc.append(doc_dict)
            sample['documents'] = doc

    with open(savepath, 'w', encoding='utf-8') as f:
        for i in first_ans:
            f.write(json.dumps(i, ensure_ascii=False))
            f.write('\n')
        # f.write(json.dumps(first_ans, ensure_ascii=False))
        # json.dump(first_ans, f)


if __name__ == '__main__':
    filename = '../data/nju/ExportJSON.json'
    samplefile = '../data/nju/1_format.json'
    savefile = '../data/nju/test.json'
    savefile_wordlevel = '../data/nju/test_word_level.json'
    load(filename, samplefile, savefile)
    # di = json.loads
    # load_word_level(filename, samplefile, savefile_wordlevel)
