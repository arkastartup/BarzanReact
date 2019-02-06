

function testFunc(params) {
    var el = document.getElementById("user").value;
    var ps = document.getElementById("pass").value;

    if (!el && !ps) {
        window.alert("نام کاربری یا رمز عبور وارد نشده است")
    }
    else {
        $.ajax({
            url: "http://127.0.0.1:8000/ed/",
            data: JSON.stringify({ "state": "signin", "username": el, "password": ps }),
            type: "POST",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (data) {
                var status = data.status;
                if (status == "success") {
                    localStorage.setItem("userr", el);
                    localStorage.setItem("passs", ps);
                    window.alert("با موفقیت وارد شدید");
                    document.getElementById("logi").style.visibility = 'hidden';
                    document.getElementById("logu").style.visibility = 'visible';
                    document.getElementById("submenu").style.visibility = 'visible';
                    
                    $("nav").addClass("fixed-top");
                    document.getElementById("a2").src = 'img_avatar1.png';
                    document.getElementById("f1").reset();
                    document.getElementById("cloe").click();


                }
                else {
                    alert(status);
                }




            }

        })




    }
}
function signu() {
    window.open('signup','_self')
}
function ex() {
    location.reload();
    localStorage.setItem("userr", 0);
    localStorage.setItem("passs", 0);
}
function auto() {
    var elo = localStorage.getItem("userr");
    var psd = localStorage.getItem("passs");
    $.ajax({
        url: "http://127.0.0.1:8000/ed/",
        data: JSON.stringify({ "state": "signin", "username": elo, "password": psd }),
        type: "POST",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            var status = data.status;
            if (status == "success") {


                document.getElementById("logi").style.visibility = 'hidden';
                document.getElementById("logu").style.visibility = 'visible';
                document.getElementById("submenu").style.visibility = 'visible';
                $("nav").addClass("fixed-top");
                document.getElementById("a2").src = 'img_avatar1.png';
                document.getElementById("f1").reset();
                document.getElementById("cloe").click();


            }





        }

    })

}


auto();