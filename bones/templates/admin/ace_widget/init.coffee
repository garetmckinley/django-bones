scripts = document.getElementsByTagName('script');
_THIS = scripts[scripts.length - 1].src;
_ID = Math.floor((Math.random() * 10000) + 1)

gup = (name) ->
  name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]")
  regexS = "[\\?&]" + name + "=([^&#]*)"
  regex = new RegExp(regexS)
  results = regex.exec(_THIS)
  unless results?
    null
  else
    results[1].split "+"

langs = gup("lang")
fields = gup("field")
labels = gup("label")
rendered_ace = false


cssSuccess = (template, field, label, lang) ->
  (data, textStatus, jqXHR) ->
    row = $(".field-"+field)
    content = $("#id_"+field).val()
    row.html("loading widget...")

    css = data.replace(new RegExp("__FIELD__", 'g'), field)
    html = template.replace(new RegExp("__FIELD__", 'g'), field)
    html = html.replace(new RegExp("__LABEL__", 'g'), label)
    html = "<style>" + css + "</style>" + html



    row.html html
    editor = ace.edit("ace_"+field+"_editor")
    editor.setTheme("ace/theme/tomorrow")

    editor.getSession().setMode("ace/mode/"+lang)
    raw = $("#id_"+field)
    editor.setValue content, 1
    raw.val content
    editor.getSession().on "change", ->
      raw.val editor.getSession().getValue()


templateSuccess = (field, label, lang) ->
  (data, textStatus, jqXHR) ->
    $.ajax
      async: false
      type: "GET"
      url: "/static/bones/admin/ace_widget/style.css"
      success: cssSuccess(data, field, label, lang)




$ ->
  if rendered_ace is false
    rendered_ace = true
    i = 0
    while i < langs.length
      $.ajax
        async: false
        type: "GET"
        url: "/static/bones/admin/ace_widget/view.html"
        success: templateSuccess(fields[i], decodeURIComponent(labels[i]), langs[i])
      i++


