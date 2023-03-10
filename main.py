import streamlit as st

# Def for calculate
def calculate_score(bmi, asa, hct, laminec, tlif, sacral):
    ##Classified score group
    if bmi <= 25:
        bmi_s = 0
    else:
        bmi_s = 2
    if asa <= 2:
        asa_s = 0
    else:
        asa_s = 1
    if hct <= 38:
        hct_s = 0
    else:
        hct_s = -3.5
    if laminec <= 1:
        laminec_s = 0
    elif laminec == 2:
        laminec_s = 4
    else:
        laminec_s = 10
    if tlif <= 1:
        tlif_s = 0
    else:
        tlif_s = 3
    if sacral == 'no':
        sacral_s = 0
    else:
        sacral_s = 3

    ##Calculate score
    score_prc = bmi_s + asa_s + hct_s + laminec_s + tlif_s + sacral_s
    if score_prc <= 6:
        n_prc = 1
    elif score_prc >= 6.5:
        n_prc = 2
    return n_prc, score_prc


# Part of Web
st.header('Lumbar spine surgery PRC Prediction')
st.caption('อ.นายแพทย์ชัชวาลย์ ไพโรจน์')

with st.sidebar:
    st.write('**Predictor Model V.1**')
    st.write('Sensitivity 84.07%')
    st.write('Sepcificity 83.68%')
    st.write('Positive predictive value 85.97%')
    st.write('Negative predictive value 81.54%')

col1, col2 = st.columns(2)
with col1:
    hn = st.text_input('HN')
    weight = st.number_input('Weight (kg)')
    height = st.number_input('Height (cm.)')
    asa = st.radio('ASA Classification', [1, 2, 3, 4 ,5 ,6])

with col2:
    hct = st.number_input('Pre-op Hct (%)')
    laminec = st.radio('Laminectomy (level)', [0, 1, 2 , 'more than 3'])
    tlif = st.radio('TLIF (level)',[0, 1, 'more than 1'])
    sacral = st.radio('ผ่าถึงระดับ Sacral (Sacral inclusion)', ['no', 'yes'])

if st.button('Make prediction'):
    bmi = weight/((height/100)**2)
    prc, output_score = calculate_score(bmi, asa, hct, laminec, tlif, sacral)
    st.subheader(f'HN: {hn}')
    st.write(f'Suggest Crossmatching :red[**{prc}**] unit')
    st.write(f'Calculated Score for this patient is: {output_score}')
