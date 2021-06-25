# 小雞上工任務 python-client

小雞上工任務一定要用App才能接案，所以做了一個python client來自動接案

function|description
--|---|
chickpt(login_key,m_id)|使用cookie登入
chickpt.sms_login(phone_num)|使用電話登入(互動式輸入驗證碼)|
chickpt.search_case(keyword)|查詢案子|
chickpt.get_resume(job_id)|查接案問題|
chickpt.apply_case(job_id,bio,questions)|接案|
