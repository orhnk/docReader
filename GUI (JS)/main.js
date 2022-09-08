// const { spawn } = require('child_process');
import { spawn } from 'child_process'
var input = document.getElementById("search");

var communicate = {type: "NaN",
    path: "NaN",
    search: "NaN"};

var supported = false;

document.getElementById('search')
    .style.visibility = "hidden";

searchElement = document.getElementById('inputfile')

searchElement.addEventListener('change', function() {

        var fr=new FileReader();
        fr.onload=function(){
            files = document.getElementById('inputfile').files;
            if (files[0].name.slice(-4) == ".txt" ||files[0].name.slice(-3) == ".rs"  ||files[0].name.slice(-3) == ".py" ||files[0].name.slice(-3) == ".js" ||files[0].name.slice(-3) == ".sh" ||files[0].name.slice(-2) == ".c" ||files[0].name.slice(-4) == ".cpp"  ) {
                // Spechial char filter
                data = fr.result.replace("?", " ");
                data = data.replace("\"", " ");
                data = data.replace("\\", " ");
                data = data.replace("'", " ");
                data = data.replace(")", " ");
                data = data.replace("(", " ");
                data = data.replace("{", " ");
                data = data.replace("}", " ");
                data = data.replace("/", " ");
                data = data.replace(".", " ");
                data = data.replace("<", " ");
                data = data.replace(">", " ");
                data = data.replace("*", " ");
                data = data.replace("+", " ");
                data = data.replace(",", " ");
                data = data.replace(";", " ");
                data = data.replace("~", " ");
                data = data.replace(":", " ");
                data = data.replace("=", " ");
                data = data.replace("#", " ");
                data = data.replace("\"", " ");
                array = data.split(/\s+/);
                document.getElementById('graph')
                    .textContent=fr.result;
                // console.log("that is a text")
                supported = true;
            }
            else if (files[0].name.slice(-4) == ".pdf") {
                // console.log("that's a pdf");
                // call python
                // communicate['type'] = "pdf";
                // communicate['path'] = searchElement.value;
                console.log("spawning...")
                pydf = spawn('python', [pdf.py]);
                console.log("spawned")
                pydf.stdout.on('data', function (data) {
                    document.getElementById('ret')
                        .textContent = data + "found";
                })
                console.log("done");

                supported = true;
                window.open(fr.result.pdf);
            }
            else if (files[0].name.slice(-4) == ".jpg" || files[0].name.slice(-5) == ".jpeg" || files[0].name.slice(-4) == ".png" || files[0].name.slice(-5) == ".webp" ) {
                // console.log("that's an image");
                //
                // Call Python
                supported = true;
            }
            else {
                supported = false;
                alert("This type of file is not supported by this site")
            }

            if (supported) {
                document.getElementById('search')
                    .style.visibility = "visible";
            }
            else {
                document.getElementById('search')
                    .style.visibility = "invisible";
            }
        }
        // data = fr.result;

        fr.readAsText(this.files[0]);
    })




// function uploadFiles() {
//     files = document.getElementById('inputfile').files;
//     if(files.length==0){
//         alert("Please first choose or drop any file(s)...");
//         return;
//     }
//     var filenames="";
//     for(var i=0;i<files.length;i++){
//         filenames+=files[i].name+"\n";
// document.getElementById("inputfile")
//     .addEventListener('change', function() {

//         var fr=new FileReader();
//         fr.onload=function(){
//             document.getElementById('output')
//                 .textContent=fr.result;
//         }

//         fr.readAsText(this.files[0]);
//     })
// }
// alert("Selected file(s) :\n"+filenames);

// console.log(files);
// console.log(data);

// Talk to python:
// data.sendTo(python);

// Preview before download.
// }

input.addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        // document.getElementById("myBtn").click();
        search = input.value;


        // data = fr.result.split("?", "");
        // data = data.split("\"", "");
        // data = data.split("\\", "");
        // data = data.split("'", "");
        // data = data.split(")", "");
        // data = data.split("(", "");
        // data = data.split("{", "");
        // data = data.split("}", "");
        // data = data.split("/", "");
        // data = data.split("<", "");
        // data = data.split(">", "");
        // data = data.split("*", "");
        // data = data.split("+", "");
        // data = data.split(",", "");
        // data = data.split(";", "");
        // data = data.split("~", "");
        // data = data.split(":", "");
        // data = data.split("=", "");
        // data = data.split("#", "");

        for (var i = 0; i < array.length; i++) {
            // data = data.split(".", "");
            if (search == array[i]) {
                alert("Got It!");
                document.getElementById('ret')
                    .textContent = search + " found!"
                break;
            }
        }
    }
}); 
