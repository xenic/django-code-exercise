//TODO: switch everything from jQuery to plain JavaScript...  except ajax.

$("#administration").click(function(){ window.location = "/admin/"; });
$("#adminCreateClass").click(function(){ window.location = "/admin/gk_attendance/schoolclass/add/"; });
$("#adminCreateStudent").click(function(){ window.location = "/admin/gk_attendance/student/add/"; });
$("#adminCreateTeacher").click(function(){ window.location = "/admin/gk_attendance/student/add/"; });
$("#administration").click(function(){ window.location = "/admin/"; });

function displayClassList(action){
  let settings = {url:'/api/school_class/'}
  $.ajax(settings).done(function(results){
    $("#additionalData").empty();
    $("#additionalData").text("Which Class?");
    let newList = $("<ul>");
    for(let i = 0; i < results.length; i++){
      let newLi = $("<li>");
      newLi.text(results[i].name);
      newLi.attr("class_id", results[i].id);
      newLi.click(action);
      newList.append(newLi);
    }
    $("#additionalData").append(newList);
  })
}

function loadStudents(e){
  let classId = e.target.getAttribute("class_id");
  $("#additionalData").empty().text(e.target.innerHTML);
  let settings = {url:'/studentListByClass/'+classId+'/'}
  $.ajax(settings).done(function(results){
    //let content = document.getElementById("content");
    //content.innerHTML = "";
    //let date_input = document.createElement("input")
    //date_input.type = "date";
    //content.append(date_input)

    let content = $("#content");
    content.empty();
    let date_input = $("<input>");
    date_input.attr("type", "date");
    content.append(date_input);
    let studentTable = $("<table>");
    for(let i = 0; i < results.length; i++){
      let newRow = $("<tr>");
      let studentCol = $("<td>");
      studentCol.text(results[i].first_name + " " + results[i].last_name);
      //TODO: make this not terrible...  also read statuses from api endpoint.
      let studentAtt = $("<td>");
      let present = $("<input>").attr("name", "att"+results[i].id);
      let tardy = $("<input>").attr("name", "att"+results[i].id);
      let absent = $("<input>").attr("name", "att"+results[i].id);
      present.attr("type", "radio");
      tardy.attr("type", "radio");
      absent.attr("type", "radio");
      let presentText = $("<span>").text("present");
      let tardyText = $("<span>").text("tardy");
      let absentText = $("<span>").text("absent");
      studentAtt.append(present)
      studentAtt.append(presentText)
      studentAtt.append(tardy)
      studentAtt.append(tardyText)
      studentAtt.append(absent)
      studentAtt.append(absentText)
      newRow.append(studentCol);
      newRow.append(studentAtt);
      studentTable.append(newRow)
    }
    $("#content").append(studentTable);
  })

}


$("#studentAttendanceByClass").click(function(){
  //view student attendance by class
  displayClassList();
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
  displayClassList(loadStudents);
});



function showStudentsByClass(e){
  let classId = e.target.getAttribute("class_id");

}
