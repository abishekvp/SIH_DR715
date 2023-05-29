const model = document.querySelector('#connect');
    const openModel = document.querySelector('.start');
    const closeModel = document.querySelector('.end');

    openModel.addEventListener('click',()=> {
        model.showModal();
        console.log("hello");
    })
    closeModel.addEventListener('click', ()=>{
        model.close();
    })


    const profile_model = document.querySelector('#update');
             const profile_openModel = document.querySelector('.open');
             const profile_closeModel = document.querySelector('.close-dia');
         
             openModel.addEventListener('click',()=> {
                 profile_model.showModal();
             })
             closeModel.addEventListener('click', ()=>{
                 profile_model.close();
             })