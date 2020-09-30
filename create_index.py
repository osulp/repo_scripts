import glob2
import os
path = '/data0/hydra/shared/tmp/bags/etd/2020'
baseurl = 'http://osul-mastaging.library.oregonstate.edu/'

# find all Bag directories in path
# create index.html in path
def write_main_index(path):
  content = ''
  dirs = glob2.glob("{}/*".format(path), recursive=False)
  #dirs = [os.path.join(path, o) for o in os.listdir(path) 
  #                  if os.path.isdir(os.path.join(path,o))]
  main_index_file = "{}/index.html".format(path)
  f = open(main_index_file, 'w')
  for dir in dirs:
    if os.path.isdir(dir): 
      item = "{}{}".format('', dir).replace("/data0/hydra/shared/tmp/bags/", baseurl)
      content += '<li><a href="{}">{}</a></li>\n'.format(item, item)
      # if movw write in for, then it will be output subdirectories incrementally
      # link to sub1
      # 
      # link to sub1
      # link to sub2
      # 
      # link to sub1
      # link to sub2
      # link to sub3  
      # f.write(get_page(content))
      write_bag_index(dir)
  f.write(get_page(content))
  f.close()
  print "DONE"

# go to each Bag directory
# get all .txt
# get everything in data
# create data.zip for data directory
# create index.html in Bag
def write_bag_index(dir):
  content = ''
  files = [f for f in glob2.glob(dir + "**/*.txt", recursive=False)]
  data = os.path.join(dir, 'data')
  files.extend(glob2.glob(data + "**/*.*", recursive=True))
  cmd = "zip -r " + dir + "/data.zip " + data
  os.system(cmd) 
  files.append(dir + "/data.zip")
  index_file = "{}/index.html".format(dir)
  f = open(index_file, 'w')
  for file in files:
    item = "{}{}".format('', file).replace("/data0/hydra/shared/tmp/bags/", baseurl)
    content += '<li><a href="{}">{}</a></li>\n'.format(item, item)
  f.write(get_page(content))  
  f.close()




def get_page(content):
  return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
<ul>
{}
</ul>
</body>
</html>""".format(content)


write_main_index(path)
