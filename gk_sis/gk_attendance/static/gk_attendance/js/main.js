let content = $("#content");

$("#administration").click(function(){ window.location = "/admin/"; });
$("#adminCreateClass").click(function(){ window.location = "/admin/gk_attendance/schoolclass/add/"; });
$("#adminCreateStudent").click(function(){ window.location = "/admin/gk_attendance/student/add/"; });
$("#adminCreateTeacher").click(function(){ window.location = "/admin/gk_attendance/student/add/"; });
$("#administration").click(function(){ window.location = "/admin/"; });


$("#studentAttendanceByClass").click(function(){
  //view student attendance by class
  let settings = {url:'/api/school_class/'}
  $.ajax(settings).done(function(results){
    $("#additionalData").empty();
    $("#additionalData").text("Which Class?");
    let newList = $("<ul>");
    for(let i = 0; i < results.length; i++){
      let newLi = $("<li>");
      newLi.text(results[i].name);
      newLi.attr("class_id", results[i].id);
      newLi.click(showStudentsByClass);
      newList.append(newLi);
    }
    $("#additionalData").append(newList);
  })
});

$("#studentAttendanceByGrade").click(function(){
  //view student attendance by grade
});

$("#studentAttendance").click(function(){
  //view student attendance for the entire school
});

$("#studentAttendanceByStudent").click(function(){
  //view a specific student’s attendance
});

$("#markAttendance").click(function(){
  //mark attendance
});


function showStudentsByClass(e){
  let classId = e.target.getAttribute("class_id");
  
}
