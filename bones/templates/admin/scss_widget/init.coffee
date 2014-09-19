$ ->
  row = $(".field-scss_input")
  content = $("#id_scss_input").val()
  row.html("loading widget...")
  $.get '/static/bones/admin/scss_widget/view.html', (data) ->
    row.html(data)
    editor = ace.edit("scss_input-editor")
    editor.setTheme("ace/theme/tomorrow")

    editor.getSession().setMode("ace/mode/scss")
    raw = $("#id_scss_input")
    editor.setValue(content, 1)
    raw.val(content)
    editor.getSession().on "change", ->
      raw.val(editor.getSession().getValue())
      return


