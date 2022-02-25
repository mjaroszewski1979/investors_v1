function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var activeItem = null
var list_snapshot = []

buildList()

function buildList(){
    var wrapper = document.getElementById('list-wrapper')
    //wrapper.innerHTML = ''



    var url = 'http://127.0.0.1:8000/api/investor-list/'

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
        console.log('Data:', data)

        var list = data
        for (var i in list){


            try{
                document.getElementById(`data-row-${i}`).remove()
            }catch(err){

            }
    


            var full_name = `<span class="full_name">${list[i].full_name}</span>`


            var item = `
                <div id="data-row-${i}" class="task-wrapper flex-wrapper">
                    <div style="margin-bottom: 1em;">
                        ${full_name}
                    </div>
                    <ul class="actions">
                    <li><button class="button small icon solid fas fa-edit edit">Edit </button></li>
                    <li><button class="button small icon solid fal fa-trash-alt delete">Delete</button></li>
                    </ul>
                </div>
            `
            wrapper.innerHTML += item

        }

        if (list_snapshot.length > list.length){
            for (var i = list.length; i < list_snapshot.length; i++){
                document.getElementById(`data-row-${i}`).remove()
            }
        }

        list_snapshot = list


        for (var i in list){
            var editBtn = document.getElementsByClassName('edit')[i]
            var deleteBtn = document.getElementsByClassName('delete')[i]
            var full_name = document.getElementsByClassName('full_name')[i]


            editBtn.addEventListener('click', (function(item){
                return function(){
                    editItem(item)
                }
            })(list[i]))


            deleteBtn.addEventListener('click', (function(item){
                return function(){
                    deleteItem(item)
                }
            })(list[i]))


        }


    })
}


var form = document.getElementById('form-wrapper')
form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Form submitted')
    var url = 'http://127.0.0.1:8000/api/investor-create/'
    if (activeItem != null){
        var url = `http://127.0.0.1:8000/api/investor-update/${activeItem.id}/`
        activeItem = null
    }



    var full_name = document.getElementById('full_name').value
    fetch(url, {
        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'full_name':full_name})
    }
    ).then(function(response){
        buildList()
        document.getElementById('form').reset()
    })
})




function editItem(item){
    console.log('Item clicked:', item)
    activeItem = item
    document.getElementById('full_name').value = activeItem.full_name
}


function deleteItem(item){
    console.log('Delete clicked')
    fetch(`http://127.0.0.1:8000/api/investor-delete/${item.id}/`, {
        method:'DELETE', 
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        }
    }).then((response) => {
        buildList()
    })
}