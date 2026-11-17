import streamlit as st

st.set_page_config(page_title="ViaQuote HttpOnly Cloud Probe")

st.title("ViaQuote - HttpOnly Cloud Probe")

st.subheader("Teste de cookies")

st.write("Ambiente isolado. Sem Supabase e sem credenciais.")

cookie = st.context.cookies.get("vq_probe")

if cookie:
    st.success("Cookie recebido pelo Streamlit.")
    st.write("Valor:", cookie)
else:
    st.warning("Cookie ainda nao recebido pelo Streamlit.")

st.divider()

st.markdown("[1 - Criar cookie HttpOnly](/probe/set)")

st.markdown("[2 - Consultar cookie no servidor](/probe/read)")

st.markdown("[3 - Eliminar cookie](/probe/delete)")

st.divider()

st.write("Streamlit:", st.__version__)
