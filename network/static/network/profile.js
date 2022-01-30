document.querySelectorAll('.edit').forEach(edit => {
    edit.onclick = () => {
        const id = edit.dataset.id;
        edit.classList.add("d-none");
        const postContent = edit.parentElement.querySelector('.content');
        const form = edit.parentElement.querySelector('.form');
        form.querySelector('textarea').value = postContent.innerText;
        postContent.classList.add("d-none");
        form.classList.remove("d-none");
        form.onsubmit = () =>{
            const content= form.querySelector('#post-content').value;
            postContent.innerText = content;
            fetch(`/update/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    "toUpdate": "post",
                    "content": content
                })
            })
            .then(()=>{
                postContent.classList.remove("d-none");
                edit.classList.remove("d-none");
                form.classList.add("d-none");
            });
            return false;
        };
    };
});

document.querySelector('.follow').onclick = () => {
    const btn = document.querySelector('.follow');
    const id = btn.dataset.id;
    followers = document.querySelector('.followers');
    let followersCount = parseInt(followers.innerText);
    fetch(`/update/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            "toUpdate": "follow",
        })
    })
    .then(()=>{
        if(btn.innerText === 'Follow'){
            btn.innerText = 'Unfollow';
            followersCount++;
        } else{
            btn.innerText = 'Follow';
            followersCount--;
        }
        followers.innerText = followersCount;
    });
};