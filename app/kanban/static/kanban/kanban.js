let project_subroute = "/prai_information_desk";

function drag(ev) {
  ev.dataTransfer.setData("dragged_element_id", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var dragged_element_id = ev.dataTransfer.getData("dragged_element_id");
  var par = $(event.target).parent();//parent of dropzone (event.target)
  var project_stage = par.parent().parent()[0].attributes["id"].value;

  $.post(project_subroute+'/kanban/move_project_to', {'project_stage': project_stage, "research_project_pk":dragged_element_id, 'csrfmiddlewaretoken': csrftoken});
  par.after($("#" + dragged_element_id));
  clearDrop(ev);//for styling
}

//The following two functions add/remove the class droppable such that the style changes on drag-hover
const allowDrop = (ev) => {
  ev.preventDefault();
  if (hasClass(ev.target,"dropzone")) {
    addClass(ev.target,"droppable");
  }
}

const clearDrop = (ev) => {
    removeClass(ev.target,"droppable");
}

// Helpers for adding and removing classes for styling
function hasClass(target, className) {
    return new RegExp('(\\s|^)' + className + '(\\s|$)').test(target.className);
}

function addClass(ele,cls) {
  if (!hasClass(ele,cls)) ele.className += " "+cls;
}

function removeClass(ele,cls) {
  if (hasClass(ele,cls)) {
    var reg = new RegExp('(\\s|^)'+cls+'(\\s|$)');
    ele.className=ele.className.replace(reg,' ');
  }
}

function unwrap(node) {
    node.replaceWith(...node.childNodes);
}
