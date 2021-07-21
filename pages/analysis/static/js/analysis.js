console.log('inside analysis');

function getText(){
    fetch('/analysis/list')
        .then((res) => res.json())
        .then((data) => {
            // console.log(data);
            let output_str = '';
            for (let item of data) {
                output_str += `<li>${item}</li>`
            }
            document.getElementById('ol1').innerHTML = `${output_str}`;
            // document.getElementById('output1').innerHTML = data;
        })
        .catch((err) => console.log(err))
}

// let n = 1;
// while (n < 100) {
//     n++;
//
//     setTimeout(getText, 1000 * n);
// }

setInterval(getText,1000);