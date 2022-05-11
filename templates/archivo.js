function renderChart() {
    const ctx1 = document.querySelector('#chart1').getContext('2d')
    datar1(ctx1)
    const ctx2 = document.querySelector('#chart2').getContext('2d')
    datar2(ctx2)
}



function datar2(ctx){

    async function getHum() {
        let headersList = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)"
        };

        const request = await fetch("http://192.168.0.17:8000/getTemp", {
            method: "GET",
            headers: headersList
        });

        return await request.json();
    };

    let a = getHum();

    a.then(data => {

        let temperatura = data ? Object.values(data).map(item => item.temperatura) : null;

        console.log(temperatura)

        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: temperatura,

                datasets: [
                    {
                        label: 'Humedad',
                        borderColor: '#348feb',
                        data: temperatura,
                        tension: 0.1,
                    }
                ]
            }
        })

    })


}


function datar1(ctx){

    async function getHum() {
        let headersList = {
            "Accept": "*/*",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)"
        };

        const request = await fetch("http://192.168.0.17:8000/getHum", {
            method: "GET",
            headers: headersList
        });

        return await request.json();
    };

    let a = getHum();

    a.then(data => {

        let humedad = data ? Object.values(data).map(item => item.humedad) : null;

        console.log(humedad)

        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: humedad,

                datasets: [
                    {
                        label: 'Humedad',
                        borderColor: '#348feb',
                        pointBorderColor: '#2a12ff',
                        hoverBorderColor: '#2a12ff',
                        data: humedad,
                        tension: 0.1,
                    }
                ]
            }
        })
        
    })
}

renderChart()





