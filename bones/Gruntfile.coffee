module.exports = (grunt) ->
  template = @option("template" || 'default')
  static_path = @option("static" || '')

  fs = require 'fs'
  isModified = (filepath) ->
    now = new Date()
    modified =  fs.statSync(filepath).mtime
    return (now - modified) < 10000

  @initConfig
    watch:
      options:
        livereload: true
      css:
        files: ['templates/'+template+'/scss/*.scss']
        tasks: ['compass']
      coffeescript:
        files: ['templates/admin/'+template+'/*.coffee']
        tasks: 'coffee:modified'
      widget:
        files: ['templates/admin/'+template+'/*.jade',
          'templates/admin/'+template+'/*.coffee'
          'templates/admin/'+template+'/*.scss']
        tasks: ['jade:modified', 'coffee:modified', 'compass:widget']
      admin:
        files: ['static/admin/css/*.scss']
        tasks: 'compass:admin'

    compass:
      dist:
        options:
          sassDir: 'templates/'+template+'/scss/'
          cssDir: static_path+'/bones/templates/'+template+'/css/'
      widget:
        options:
          sassDir: 'templates/admin/'+template
          cssDir: static_path+'/bones/admin/'+template
      admin:
        options:
          sassDir: 'static/admin/css/'
          cssDir: static_path+'/admin/css/'

    coffee:
      options:
        sourceMap: true
        bare: true
        force: true
      all:
        expand: true
        cwd: 'templates/admin/'+template
        src: '**/*.coffee'
        dest: static_path+'/bones/admin/'+template
        ext: '.js'
      modified:
        expand: true
        cwd: 'templates/admin/'+template
        src: '**/*.coffee'
        dest: static_path+'/bones/admin/'+template
        ext: '.js'
        filter: isModified


    jade:
      all:
        cwd: 'templates/admin/'+template
        src: '**/*.jade'
        dest: static_path+'/bones/admin/'+template
        ext: '.html'
      modified:
        expand: true
        cwd: 'templates/admin/'+template
        src: '**/*.jade'
        dest: static_path+'/bones/admin/'+template
        ext: '.html'
        filter: isModified





  @loadNpmTasks("grunt-contrib-watch")
  @loadNpmTasks("grunt-contrib-compass")
  @loadNpmTasks("grunt-contrib-coffee")
  @loadNpmTasks("grunt-contrib-jade")
  @registerTask "default", ["watch", "compass", "coffee:all", "jade:all"]
