from django.http import HttpResponse
from django.shortcuts import render

data = {
    'CourseCategories': [
        { 'id': 1 ,'name': 'Programming', 'totalCourses': 4},
        { 'id': 2 ,'name': 'Graphic Design', 'totalCourses': 3},
        { 'id': 3 ,'name': 'Video Editing', 'totalCourses': 3},
        { 'id': 4 ,'name': 'Online Marketing', 'totalCourses': 3}
 
    ],
    'Instructors' : [
        {'name': 'Andrew Smith', 'designation': 'Python Trainer', 
            'facebookLink':'facebook.com', 'twitterLink':'twitter.com', 
            'instagramLink':'instagram.com'},
        {'name': 'Monica Jackson', 'designation': 'Java Trainer', 
            'facebookLink':'facebook.com', 'twitterLink':'twitter.com', 
            'instagramLink':'instagram.com'},
        {'name': 'Henry Jacob', 'designation': 'C++ Trainer', 
            'facebookLink':'facebook.com', 'twitterLink':'twitter.com', 
            'instagramLink':'instagram.co3m'},
        {'name': 'Stella D\'souza', 'designation': 'Design Trainer', 
            'facebookLink':'facebook.com', 'twitterLink':'twitter.com', 
            'instagramLink':'instagram.com'}
    ],
    'courseList' : {
        'Programming': [
            {'name': 'Python', 'fees': '$140', 'teacher':'Andrew Smith', 'duration': '21', 'batch': 30, 'popular':'no'},
            {'name': 'Java', 'fees': '$140', 'teacher':'Monica Jackson', 'duration': '15', 'batch': 30, 'popular':'yes'},
            {'name': 'C++', 'fees': '$140', 'teacher':'Henry Jacob', 'duration': '18', 'batch': 30, 'popular':'no'}
        ],
        'Graphic Design': [
            {'name': 'Canva', 'fees': '$140', 'teacher':'Stella D\'souza', 'duration': '21', 'batch': 30, 'popular':'yes'},
            {'name': 'Adobe Photoshop', 'fees': '$140', 'teacher':'Stella D\'souza', 'duration': '15', 'batch': 30, 'popular':'no'},
            {'name': 'Figma', 'fees': '$140', 'teacher':'Stella D\'souza', 'duration': '12', 'batch': 30, 'popular':'no'}
        ],
        'Video Editing': [
            {'name': 'Capcut', 'fees': '$140', 'teacher':'Stella D\'souza', 'duration': '21', 'batch': 30, 'popular':'no'},
            {'name': 'Adobe Premier', 'fees': '$140', 'teacher':'Stella D\'souza', 'duration': '15', 'batch': 30, 'popular':'no'},
            {'name': 'YouTube', 'fees': '$140', 'teacher':'Stella D\'souza', 'duration': '18', 'batch': 30, 'popular':'no'}
        ],
        'Online Marketing' :  [
            {'name': 'Digital Marketing', 'fees': '$140', 'teacher':'Anthony Rodrigues', 'duration': '21', 'batch': 30, 'popular':'no'},
            {'name': 'Social Media Marketing', 'fees': '$140', 'teacher':'Anthony Rodrigues', 'duration': '15', 'batch': 30, 'popular':'yes'},
            {'name': 'Email Marketing', 'fees': '$140', 'teacher':'Anthony Rodrigues', 'duration': '18', 'batch': 30, 'popular':'no'}
        ]
    },
    'testimonials' : [
        {'name': 'Lucy Parker', 'profession':'Java Developer at Microsoft',
         'testimonial_text': 'I thought Java was though but eLearning helped me become a Java master with it\'s comprehensive courses'},
        {'name': 'Mathew Fernandez', 'profession':'Database Administrator at Google',
         'testimonial_text': 'Becoming a database administrator is like a dream come true. eLearning made me enjoy the process of working with large database systems efficiently.'},
        {'name': 'Jason Cruz', 'profession':'C++ Developer at Oracle',
         'testimonial_text': 'I was scared to learn C++ and apply its concepts in real world. eLearning became a life changer for me, as it made me an expert C++ developer.'},
        {'name': 'Claire Lau', 'profession':'Python Developer at Salesforce',
         'testimonial_text': 'eLearning helped me learn Python in the most efficient way - by building real projects, I could stand out during interviews.'}
    ],
}

popularItems = [] 

for category in data["courseList"]:
    for item in data["courseList"][category]:
        if(item["popular"] == 'yes'):
            popularItems.append(item)


def home(request):
    # data = {
    #     'title': 'Home',
    #     'content': 'This is home page using templates'
    # }

    
    context = {
        'data': data,
        'popularItems': popularItems
    }
    
    # return HttpResponse("This is home page")\
    return render(request, "index.html", context)

def aboutus(request):
    
    context = {
        'data':data
    }
    # return HttpResponse("<p> this is about us page</p>")
    return render(request, "aboutus.html", context)

def course(request):
    context = {
        'data':data,
        'popularItems': popularItems
    }
    # return HttpResponse("<p>This is course page</p>")
    # return render(request, 'course.html', courseList)
    return render(request, 'courses.html', context)

def courseDetails(request, courseid):
    for category in data["CourseCategories"]:
        if category["id"] == courseid:
            category_name = category["name"]
            totalCourses = category["totalCourses"]
            break
    for category in data["courseList"]:
        if category == category_name:
            courseItems = data["courseList"][category]
            break
    courseData = {
        'courseid': courseid,
        'category_name': category_name,
        'totalCourses' : totalCourses,
        'courseItems': courseItems
    }
    # return HttpResponse(courseid)
    return render(request, 'courseDetails.html', courseData)

def ourteam(request):
    context = {
        'data': data
    }
    return render(request, 'team.html', context)

def testimonial(request):
    context = {
        'data': data
    }
    return render(request, 'testimonial.html', context)

def contact(request):
    return render(request, 'contact.html')

def pageNotFound(request, exception):
    return render(request, '404.html', status=404)