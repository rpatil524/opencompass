from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import FixKRetriever
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_evaluator import AccwithDetailsEvaluator
from opencompass.datasets import MMMLUDataset
from opencompass.utils.text_postprocessors import first_option_postprocess
from mmengine.config import read_base

with read_base():
    from .mmmlu_prompt import (get_few_shot_prompts_ar, 
                               get_few_shot_prompts_bn, 
                               get_few_shot_prompts_de, 
                               get_few_shot_prompts_es, 
                               get_few_shot_prompts_fr, 
                               get_few_shot_prompts_hi, 
                               get_few_shot_prompts_id,         
                               get_few_shot_prompts_it,
                               get_few_shot_prompts_ja, 
                               get_few_shot_prompts_ko, 
                               get_few_shot_prompts_pt, 
                               get_few_shot_prompts_zh, 
                               get_few_shot_prompts_sw, 
                               get_few_shot_prompts_yo)

mmmlu_reader_cfg = dict(
    input_columns=['input', 'A', 'B', 'C', 'D','subject'],
    output_column='target',
    train_split='test')

mmmlu_all_sets = [
    'mmlu_AR-XY',
    'mmlu_BN-BD',
    'mmlu_DE-DE',
    'mmlu_ES-LA',
    'mmlu_FR-FR',
    'mmlu_HI-IN',
    'mmlu_ID-ID',
    'mmlu_IT-IT',
    'mmlu_JA-JP',
    'mmlu_KO-KR',
    'mmlu_PT-BR',
    'mmlu_SW-KE',
    'mmlu_YO-NG',
    'mmlu_ZH-CN',
]

mmmlu_datasets = []
for _name in mmmlu_all_sets:
    if 'AR' in _name:
        _hint = f'هناك سؤال اختيار واحد. أجب عن السؤال بالرد على A أو B أو C أو D, يرجى استخدام واحدة من الرموز A، B، C، أو D لتمثيل خيارات الإجابة في ردك'
        _prompt = f'يتعلق بـ {{subject}} \nالسؤال: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nالإجابة:'
        _round = get_few_shot_prompts_ar(_hint, _prompt)
    elif 'BN' in _name:
        _hint = f'এটি একটি একক পছন্দের প্রশ্ন। এ, বি, সি বা ডি উত্তর দিয়ে প্রশ্নের উত্তর দিন।, আপনার উত্তরে ইংরেজি বর্ণ A, B, C এবং D এর মধ্যে একটি ব্যবহার করুন'
        _prompt = f'এটি {{subject}} সম্পর্কে \nপ্রশ্ন: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nউত্তর:'
        _round = get_few_shot_prompts_bn(_hint, _prompt)
    elif 'DE' in _name:
        _hint = f'Es gibt eine Einzelwahlfrage. Beantworte die Frage, indem du A, B, C oder D antwortest.'
        _prompt = f'Es geht um {{subject}} \nFrage: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nAntwort:'
        _round = get_few_shot_prompts_de(_hint, _prompt)
    elif 'ES' in _name:
        _hint = f'Hay una pregunta de elección única. Responde a la pregunta respondiendo A, B, C o D.'
        _prompt = f'Se trata de {{subject}} \nPregunta: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nRespuesta:'
        _round = get_few_shot_prompts_es(_hint, _prompt)
    elif 'FR' in _name:
        _hint = f'Il y a une question à choix unique. Répondez à la question en répondant A, B, C ou D.'
        _prompt = f'''C'est à propos de {{subject}} \nQuestion : {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nRéponse :'''
        _round = get_few_shot_prompts_fr(_hint, _prompt)
    elif 'HI' in _name:
        _hint = f'यह एक एकल विकल्प प्रश्न है। प्रश्न का उत्तर A, B, C या D में से कोई भी उत्तर देकर दें।'
        _prompt = f'यह {{subject}} के बारे में है \nप्रश्न: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nउत्तर:'
        _round = get_few_shot_prompts_hi(_hint, _prompt)
    elif 'ID' in _name:
        _hint = f'Ada pertanyaan pilihan tunggal. Jawablah pertanyaan dengan menjawab A, B, C, atau D.'
        _prompt = f'Ini tentang {{subject}} \nPertanyaan: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nJawaban:'
        _round = get_few_shot_prompts_id(_hint, _prompt)
    elif 'IT' in _name:
        _hint = f'Ci sono domande a scelta singola. Rispondi alla domanda rispondendo A, B, C o D.'
        _prompt = f'Si tratta di {{subject}} \nDomanda: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nRisposta:'
        _round = get_few_shot_prompts_it(_hint, _prompt)
    elif 'JA' in _name:
        _hint = f'単一選択肢の質問があります。この質問にはA、B、C、またはDで答えてください。'
        _prompt = f'これは {{subject}} に関することです \n質問: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\n回答:'
        _round = get_few_shot_prompts_ja(_hint, _prompt)
    elif 'KO' in _name:
        _hint = f'단일 선택 질문이 있습니다. A, B, C 또는 D로 답변해 주세요.'
        _prompt = f'이것은 {{subject}}에 관한 것입니다 \n질문: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\n답변:'
        _round = get_few_shot_prompts_ko(_hint, _prompt)
    elif 'PT' in _name:
        _hint = f'Há uma pergunta de escolha única. Responda à pergunta escolhendo A, B, C ou D.'
        _prompt = f'É sobre {{subject}} \nPergunta: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nResposta:'
        _round = get_few_shot_prompts_pt(_hint, _prompt)
    elif 'ZH' in _name:
        _hint = f'这里有一个单项选择题。请通过选择 A、B、C 或 D 来回答该问题。'
        _prompt = f'这是关于 {{subject}} 的内容\n问题：{{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\n答案：'
        _round = get_few_shot_prompts_zh(_hint, _prompt)
    elif 'SW' in _name:
        _hint = f'Kuna swali moja la chaguo. Jibu swali kwa kujibu A, B, C au D.'
        _prompt = f'Hii ni kuhusu {{subject}}.\nSwali: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nJibu:'
        _round = get_few_shot_prompts_sw(_hint, _prompt)
    elif 'YO' in _name:
        _hint = f'Ibeere kan wa ti o ni yiyan kan. Fesi si ibeere naa nipa fesi A, B, C tabi D.'
        _prompt = f'Eyi jẹ nipa {{subject}}.\nIbeere: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nFesi:'
        _round = get_few_shot_prompts_yo(_hint, _prompt)
    else:
        _hint = f'There is a single choice question. Answer the question by replying A, B, C or D.'
        _prompt = f'it is about {{subject}} \nQuestion: {{input}}\nA. {{A}}\nB. {{B}}\nC. {{C}}\nD. {{D}}\nAnswer:'
        _round = f'{_hint}\n{_prompt}\n'+'Please answer only with option A, B, C or D. \nAnswer:'
    mmmlu_infer_cfg = dict(
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
                begin='</E>',
                round=_round
            ),
            ice_token='</E>',
        ),
        retriever=dict(type=ZeroRetriever),
        inferencer=dict(type=GenInferencer),
    )

    mmmlu_eval_cfg = dict(
        evaluator=dict(type=AccwithDetailsEvaluator),
        pred_postprocessor=dict(type=first_option_postprocess, options='ABCD'))

    mmmlu_datasets.append(
        dict(
            abbr=f'openai_m{_name}',
            type=MMMLUDataset,
            path='openai/MMMLU',
            name=_name,
            reader_cfg=mmmlu_reader_cfg,
            infer_cfg=mmmlu_infer_cfg,
            eval_cfg=mmmlu_eval_cfg,
        ))

del _name, _hint, _prompt, _round
