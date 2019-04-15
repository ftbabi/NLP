import json

class DataStructure:
    def __init__(self):
        self.data = {}
        self.data['documents'] = []
        self.data['answer_spans'] = []
        self.data['fake_answers'] = []
        self.data['question'] = ""
        self.data['segmented_answers'] = []
        self.data['answers'] = []
        self.data['answer_docs'] = []
        self.data['segmented_question'] = []
        self.data['question_type'] = "FACT"
        self.data['question_id'] = []
        self.data['fact_or_opinion'] = 'FACT'
        self.data['match_scores'] = []

        self.doc_p = {'is_selected': True,
                      'title': "",
                      'most_related_para': 0,
                      'segmented_title': [],
                      'segmented_paragraphs': [],
                      'paragraphs': [],
                      'bs_rank_pos': 0
                      }

    def addDoc(self, is_selected=True, title="", most_related_para=0, segmented_title=[], segmented_paragraphs=[],
               paragraphs=[], bs_rank_pos=0):
        # segmented title 指把title分词之后，以list形式保存；paragraphs是每一段单独一个列表，多个段落（列表）组成一个该参数
        # segmented paragraphs每个列表里面存对应的分词结果
        doc_p = {'is_selected': is_selected,
                      'title': title,
                      'most_related_para': most_related_para,
                      'segmented_title': segmented_title.copy(),
                      'segmented_paragraphs': segmented_paragraphs.copy(),
                      'paragraphs': paragraphs.copy(),
                      'bs_rank_pos': bs_rank_pos
                      }
        self.data['documents'].append(doc_p)

    def addAnsSpans(self, answer_spans=[]):
        self.data['answer_spans'].append(answer_spans.copy())

    def addFakeAns(self, fans=""):
        self.data['fake_answers'].append(fans)

    def addQuestion(self, q):
        self.data['question'] = q

    def addSegmentedAns(self, s_ans=[]):
        # 每次加一个答案
        self.data['segmented_answers'].append(s_ans.copy())

    def addAns(self, ans):
        self.data['answers'].append(ans)

    def addAnsDocs(self, docs):
        self.data['answer_docs'] = docs

    def addSegmentedQuestion(self, q=[]):
        self.data['segmented_question'] = q.copy()

    def addQuestionType(self, type='FACT'):
        self.data['question_type'] = type

    def addQuestionId(self, id):
        self.data['question_id'] = id

    def addFactOrOpinion(self, op="FACT"):
        self.data['fact_or_opinion'] = op

    def addMatchScores(self, scores=0):
        self.data['match_scores'].append(scores)

    def getData(self):
        return self.data


class DataProcess:
    def __init__(self, spath):
        self.spath = spath

    def convert(self, data):
        with open(self.spath) as f:
            j = json.dumps(data)
            f.write(j)
            f.write('\n')

if __name__ == '__main__':
    a = [1]
    b = []
    b.append(a.copy())
    a[0] = 2

    print(b)