from transformers import pipeline
import streamlit as st

# Оптимизация: объединение функций get_pipeline и answer_and_score в одну функцию для уменьшения количества вызовов.
def find_answer(question, context):
    if not context.strip() or not question.strip():
        raise ValueError("Both CONTEXT and QUESTION fields must be filled.")
    
    qa = pipeline('question-answering')
    result = qa(context=context, question=question)
    return result['answer'], result['score']

if __name__ == '__main__':
    try:
        st.title('ПОИСК В ТЕКСТЕ ОТВЕТА НА ВОПРОС V2.0')
        st.text('CONTEXT: текст, в котором будет осуществляться поиск ответа (только на английском).\n'
                'QUESTION: вопрос, на который будет осуществляться поиск ответа\n\t в тексте из поля CONTEXT (только на английском).')

        context = st.text_input('CONTEXT:', value='My name is Ivan.')
        question = st.text_input('QUESTION:', value='What is my name?')
        
        if st.button('ИСКАТЬ ОТВЕТ'):
            answer, score = find_answer(question, context)
            st.text(f'ANSWER={answer}\nSCORE={score}')
    except ValueError as e:
        st.text(str(e))
