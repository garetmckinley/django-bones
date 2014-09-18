$ ->
  row = $(".field-content")
  content = $("#id_content").val()
  row.html("loading widget...")
  $.get '/static/bones/admin/vue_widget/view.html', (data) ->
    row.html(data)
    new Vue(
      el: "#editor"
      data:
        input: content

      filters:
        marked: marked
    )
