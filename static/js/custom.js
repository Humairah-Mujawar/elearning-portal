// change active link in header 

let pagePath = window.location.pathname;
console.log('pagePath is ' + pagePath)

let homeNavItem = $("#home-nav");
let aboutNavItem = $("#about-nav");
let coursesNavItem = $("#courses-nav");
let contactNavItem = $("#contact-nav");
let teamNavItem = $("#team-nav");
let testimonialNavItem = $("#testimonial-nav");


switch(pagePath){
    case '/':
        homeNavItem.siblings('a').removeClass("active");
        homeNavItem.addClass('active');
        break;
    case '/aboutus/':
        aboutNavItem.siblings('a').removeClass("active");
        aboutNavItem.addClass('active');
        break;
    case '/courses/':
        coursesNavItem.siblings('a').removeClass("active");
        coursesNavItem.addClass('active');
        break;
    case '/contact/':
        contactNavItem.siblings('a').removeClass("active");
        contactNavItem.addClass('active'); 
        break;
    case '/team/':
        teamNavItem.siblings('a').removeClass("active");
        teamNavItem.addClass('active'); 
        break;
    case '/testimonial/':
        testimonialNavItem.siblings('a').removeClass("active");
        testimonialNavItem.addClass('active'); 
        break; 
    default:
        homeNavItem.siblings('a').removeClass("active");
        homeNavItem.addClass('active');
        break;

}