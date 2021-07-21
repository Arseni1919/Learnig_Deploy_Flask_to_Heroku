console.log('inside analysis');

function getText(){
    let output_str = '';
    fetch('/analysis/list')
        .then((res) => res.json())
        .then((data) => {
            // console.log(data);
            output_str = '';
            if (data.length === 0) {
                output_str += `Empty list`
            } else {
                for (let item of data) {
                    output_str += `<li>${item}</li>`
                }
            }
            document.getElementById('ol1').innerHTML = `${output_str}`;
            // document.getElementById('output1').innerHTML = data;
        })
        .catch((err) => console.log(err))
}

setInterval(getText,2000);
let output_str = '';
output_str += `Loading...`
document.getElementById('ol1').innerHTML = `${output_str}`;

// let n = 1;
// while (n < 100) {
//     n++;
//
//     setTimeout(getText, 1000 * n);
// }







