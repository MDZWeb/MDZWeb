var hamburger_id=document.querySelector('.hamburger')
var close_id=document.querySelector('.close')
var menu_items_id=document.querySelector('.menu_items')
var nav_id=document.getElementsByTagName('nav')

var service_container_left_id=document.querySelectorAll('.services .service_container .left')
var service_container_right_img_id=document.querySelectorAll('.services .right_img')

var portfolio_cat_id=document.querySelectorAll('.portfolio_cat')

var portfolio_id=document.querySelector('.portfolio')

var nav_li_id=document.querySelectorAll('.menu_items li')

var portfolio_cat_id=document.querySelectorAll('.portfolio_cat')

function window_resize(){
    window.addEventListener("resize",()=>{
        if (window.innerWidth<=1020){
            hamburger_id.style.display='block'
            close_id.style.display='none'
            menu_items_id.style.display='none'
        }
        

        else{
            hamburger_id.style.display='none'
            close_id.style.display='none'
            menu_items_id.style.display='flex'
        }
    })
}

try {
    window_resize()
} catch (error) {
    
}



hamburger_id.addEventListener('click',()=>{
    hamburger_id.style.display='none'
    close_id.style.display='block'
    menu_items_id.style.display='flex'

})

close_id.addEventListener('click',()=>{
    hamburger_id.style.display='block'
    close_id.style.display='none'
    menu_items_id.style.display='none'


    try {
        portfolio_cat_id.forEach((element,id)=>{
            element.classList.remove('active')
        })
    } catch (error) {
        
    }

})






window.addEventListener('scroll',()=>{
    if (window.scrollY>0){
        nav_id[0].classList.add('active')
    }

    else{
        nav_id[0].classList.remove('active')
    }

    if(window.innerWidth>=1024){
        if (window.scrollY>364){
            service_container_left_id[0].style.opacity='1'
            service_container_right_img_id[0].classList.add('active')
        }
    
        else{
            service_container_left_id[0].style.opacity='0'
            service_container_right_img_id[0].classList.remove('active')
        }
    
        if (window.scrollY>700){
            service_container_left_id[1].style.opacity='1'
            service_container_right_img_id[1].classList.add('active')
        }
    
        else{
            service_container_left_id[1].style.opacity='0'
            service_container_right_img_id[1].classList.remove('active')
        }
    
    
        if (window.scrollY>1000){
            service_container_left_id[2].style.opacity='1'
            service_container_right_img_id[2].classList.add('active')
        }
    
        else{
            service_container_left_id[2].style.opacity='0'
            service_container_right_img_id[2].classList.remove('active')
        }
    }

    if(window.innerWidth>500 && window.innerWidth<1024){
        if (window.scrollY>10){
            service_container_left_id[0].style.opacity='1'
            service_container_right_img_id[0].classList.add('active')
        }
    
        else{
            service_container_left_id[0].style.opacity='0'
            service_container_right_img_id[0].classList.remove('active')
        }
    
        if (window.scrollY>10){
            service_container_left_id[1].style.opacity='1'
            service_container_right_img_id[1].classList.add('active')
        }
    
        else{
            service_container_left_id[1].style.opacity='0'
            service_container_right_img_id[1].classList.remove('active')
        }
    
    
        if (window.scrollY>10){
            service_container_left_id[2].style.opacity='1'
            service_container_right_img_id[2].classList.add('active')
        }
    
        else{
            service_container_left_id[2].style.opacity='0'
            service_container_right_img_id[2].classList.remove('active')
        }
    }



    else{
        if (window.scrollY>=10){
            service_container_left_id[0].style.opacity='1'
            service_container_right_img_id[0].classList.add('active')
        }
    
        else{
            service_container_left_id[0].style.opacity='0'
            service_container_right_img_id[0].classList.remove('active')
        }
    
        if (window.scrollY>780){
            service_container_left_id[1].style.opacity='1'
            service_container_right_img_id[1].classList.add('active')
        }
    
        else{
            service_container_left_id[1].style.opacity='0'
            service_container_right_img_id[1].classList.remove('active')
        }
    
    
        if (window.scrollY>1284){
            service_container_left_id[2].style.opacity='1'
            service_container_right_img_id[2].classList.add('active')
        }
    
        else{
            service_container_left_id[2].style.opacity='0'
            service_container_right_img_id[2].classList.remove('active')
        }
    }
    
})


if(window.innerWidth<=1024){
    portfolio_id.addEventListener('click',()=>{
        portfolio_cat_id.forEach((element,id)=>{
            element.classList.toggle('active')
        })
    })
    
}


var graphic_image_popup_btn_v=document.querySelectorAll(' .graphic_designs .design_img i')
var graphic_image_v=document.querySelectorAll('.graphic_designs .design_img img')
var graphic_image_popup_img_v=document.querySelector('.pop_up_section img')
var pop_up_close_btn_v=document.querySelector('.pop_up_close')

graphic_image_popup_btn_v.forEach((element,id)=>{
    element.addEventListener('click',()=>{
        graphic_image_popup_img_v.src=graphic_image_v[id].getAttribute('src')
        document.querySelector('.pop_up_section').style.display='grid'
    })
})

pop_up_close_btn_v.addEventListener('click',()=>{
    document.querySelector('.pop_up_section').style.display='none'
})

document.querySelector('.pop_up_section').addEventListener('click',()=>{
    document.querySelector('.pop_up_section').style.display='none'
})