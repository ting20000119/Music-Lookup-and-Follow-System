function Return() {
    window.location.href = "login.html";
}
let signup = async() => {
    let account = document.getElementById("account");
    let birthYear = document.getElementById("birthYear");
    let name = document.getElementById("Name");
    let Country = document.getElementById("Country");
    let Gender = document.getElementById("Gender");

    if(birthYear.value == "") {
        window.alert("請輸入生日");
        return;
    }
    else if(Country.value == ""){
        window.alert("請輸入國家");
        return;
    }
    else if(Gender.value == ""){
        window.alert("請輸入性別");
        return;
    }
    else if(account.value == "") {
        window.alert("請輸入帳號");
        return;
    }
    else if(name.value == "") {
        window.alert("請輸入名字");
        return;
    }


    payload = {
        username: account.value,
        Name: name.value,
        Country: Country.value,
        Gender: Gender.value,
        birthYear: birthYear.value
    };

    let Status = 0;
    let Message = '';
    var url = "http://127.0.0.1:5000/register/"+account.value+"/"+name.value+"/"+birthYear.value+"/"+Gender.value+"/"+Country.value;
    console.log(url);
    let res = await fetch(url, {
        method: "GET",
        /*headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(payload)*/
    }).then(res => {
        //console.log(res.text());
        Status = res.status;
        return res.text();
    }).catch(error => {
        Message = "Something Wrong";
    });

    if(Status === 200 || Status === 201) {
        console.log("成功");
        if(res == "register success"){
            window.alert("註冊成功，請重新登入");
            window.location.href = "login.html";
        }
        else{
            window.alert("已註冊過");
        }
        //window.location.href = "login.html";
    }
    else {
        window.alert(result.message);
    }
}