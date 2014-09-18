$ ->
  row = $(".field-status_expression")
  content = $("#id_status_expression").val()
  row.html("loading widget...")
  $.get '/static/bones/admin/expression_widget/view.html', (data) ->
    row.html(data)
    editor = ace.edit("status_expression-editor")
    editor.setTheme("ace/theme/tomorrow")

    editor.getSession().setMode("ace/mode/python")
    raw = $("#id_status_expression")
    editor.setValue(content, 1)
    raw.val(content)
    editor.getSession().on "change", ->
      raw.val(editor.getSession().getValue())
      return


