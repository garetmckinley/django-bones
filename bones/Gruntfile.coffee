module.exports = (grunt) ->
  template = @option("template" || 'default')
  static_path = @option("static" || '')
  @initConfig
    watch:
      options:
        livereload: true
      #templates:
      #  files: ['jade/*.jade']
      #  tasks: ['jade']
      css:
        files: ['static/bones/templates/'+template+'/scss/*.scss']
        tasks: ['compass']

    compass:
      dist:
        options:
          sassDir: 'static/bones/templates/'+template+'/scss/'
          cssDir: static_path+'/bones/templates/'+template+'/css/'

  @loadNpmTasks("grunt-contrib-watch")
  @loadNpmTasks("grunt-contrib-compass")
  @registerTask "default", ["watch", "compass"]
