$ ->
  row = $(".field-scss")
  content = $("#id_scss").val()
  row.html("loading widget...")
  $.get '/static/bones/admin/scss_widget/view.html', (data) ->
    row.html(data)
    editor = ace.edit("scss-editor")
    editor.setTheme("ace/theme/tomorrow")

    editor.getSession().setMode("ace/mode/scss")
    raw = $("#id_scss")
    editor.setValue(content, 1)
    raw.val(content)
    editor.getSession().on "change", ->
      raw.val(editor.getSession().getValue())
      return


