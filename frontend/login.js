function Signup() {
    window.location.href = "signup.html";
}
let login = async () => {
    let account = document.getElementById("account");
    

    if (account.value == "") {
        window.alert("請輸入帳號");
        return;
    } 

    payload = {
        username: account.value,
    };
    let Status = 0;
    let Message = "";
    /*fetch 那裡放api*/ 
    var url = "http://127.0.0.1:5000/login/"+account.value;
    let res = await fetch(url, {
    method: "POST",
    headers: {
        "Content-type": "application/json",
    },
        body: JSON.stringify(payload),
    })
    .then((res) => {
        Status = res.status;
        return res.json();
    })
    .catch((error) => {
        Message = "Something Wrong";
    });
    if (Status === 200 || Status === 201) {//成功
        window.localStorage.setItem("UID", res.MID);
        window.localStorage.setItem("name", res.MName);
        window.location.href = "signup.html";
    } else {
        window.alert(res.message);
    }
}
