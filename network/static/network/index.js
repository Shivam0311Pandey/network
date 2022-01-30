document.querySelectorAll('.heart').forEach(heart =>{
    heart.style.cursor = "pointer";
    heart.onclick = () => {
        const id = heart.dataset.id;
        fetch(`/update/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                "toUpdate": "like"
            })
        })
        .then(()=>{
            let count = parseInt(document.getElementById(`${id}`).innerHTML);
            if(heart.classList.contains("bi-heart")){
                count++;
                heart.classList.remove("bi-heart");
                heart.classList.add("bi-heart-fill");
            } else{
                count--;
                heart.classList.remove("bi-heart-fill");
                heart.classList.add("bi-heart");
            }
            document.getElementById(`${id}`).innerHTML = `${count}`;
        });
    };
});