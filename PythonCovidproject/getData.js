var data;
async function getResults(){
    var statename = window.location.search.substring(1,window.location.search.length);
    var results = await fetch(`http://localhost:3000/?state=${statename}`)
    data = await results.json()
    console.log(data);
    let a= [];
    let dat = [];
    let c =[];
    let cof =[]
    for (let i = 0; i < data.length; i++) {
        c.push(data[i].Cured);
        dat.push(data[i].Date);
        a.push(data[i].Deaths);
        cof.push(data[i].Confirmed);
    }
    console.log(a);

    new Chart(document.getElementById("line-chart"), {
        type : 'line',
        data : {
            labels : dat,
            datasets : [
                    {
                        data : a,
                        label : "Death",
                        borderColor : "#BA3C3C",
                        fill : false
                    },
                    {
                        data : c,
                        label : "Cured",
                        borderColor : "#0CEB26",
                        fill : false
                    },
                    {
                        data : cof,
                        label : "Cured",
                        borderColor : "#0C10EB",
                        fill : false
                    }
                ]
        },
        options : {
            title : {
                display : true,
                text : 'Chart JS Line Chart Example'
            }
        }
    });
}

getResults();