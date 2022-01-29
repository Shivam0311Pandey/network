document.querySelectorAll('.heart').forEach(heart =>{
    heart.onclick = () => {
        const id = heart.dataset.id;
        let count = parseInt(document.getElementById(`${id}`).innerHTML);
        count++;
        document.getElementById(`${id}`).innerHTML = `${count}`;

        // fetch(`/update/${id}`, {
        //     method: 'PUT',
        //     body: JSON.stringify({
        //         "toUpdate": "like"
        //     })
        // })
        // .then(()=>{
        //     let count = parseInt(document.getElementById(`${id}`).innerHTML);
        //     count++;
        // });
    };
});