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

    let result = await fetch('http://127.0.0.1:5000/searchArtist/Aname1', {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(payload)
    }).then(res => {
        Status = res.status;
        return res.json();

    }).catch(error => {
        Message = "Something Wrong";
    });

    if(Status === 200 || Status === 201) {
        window.alert("成功");
        window.location.href = "login.html";
    }
    else {
        window.alert(result.message);
    }
}