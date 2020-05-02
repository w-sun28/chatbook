import glob
import os

from chatbook.talk import *

from chatbook.docbot import *
from chatbook.app import *

doc_dir="examples/"
doc_files = sorted(glob.glob(doc_dir+"*.txt"))
quest_files = sorted(glob.glob(doc_dir+"*_quest.txt"))

def quest2doc(qf) :
  return qf.replace('_quest.txt','.txt')

#clean files at given directory path
def clean_path(path) :
  os.makedirs(path,exist_ok=True)

  files = glob.glob(path+"/*")
  for f in files:
    os.remove(f)

def clean(force=False)  :
  D=doc_dir
  if force :
    files = glob.glob(D + "/*.json")
    for f in files:
       os.remove(f)
  files = glob.glob(D + "/*_cloud.pdf")
  for f in files:
    os.remove(f)
  files = glob.glob(D + "/*.gv.pdf")
  for f in files:
    os.remove(f)
  files = glob.glob(D + "/*.gv")
  for f in files:
    os.remove(f)
  files = glob.glob(D + "/*.pro")
  for f in files:
    os.remove(f)

# tests to run


def do(qf) :
    df=qf.replace("_quest.txt","")
    run_with(df,query=True)

def qftest() :
  do('examples/const_quest.txt')

def go()  :
  D=doc_dir
  files = sorted(glob.glob(D + "/*_quest.txt"))
  for qf in files:
    df=qf.replace("_quest.txt","")
    run_with(df,query=True)

def ftest() :
  fname='examples/geo'  #################
  run_with(fname,query=False)

def t1() :
    fname = 'examples/bfr'
    run_with(fname, query=True)


def t0():
  fname = 'examples/bfr'
  run_with(fname, query=True)

def t2():
  fname = 'examples/hindenburg'
  run_with(fname, query=True)


def t3():
  fname = 'examples/const'
  run_with(fname, query=True)

def t4():
  fname = 'examples/logrank'
  run_with(fname, query=True)

def t5():
  fname = 'examples/heaven'
  run_with(fname, query=True)

def t6():
  fname = 'examples/einstein'
  run_with(fname, query=True)

def t7():
  fname = 'examples/geo'
  run_with(fname, query=True)

def t8():
  fname = 'examples/hindenburg'
  run_with(fname, query=True)

def t9():
  fname = 'examples/kafka'
  run_with(fname, query=True)

def t10():
  fname = 'examples/test'
  run_with(fname, query=True)

def t11():
  fname = 'examples/texas'
  run_with(fname, query=True)

def t12():
  fname='examples/wasteland'  #################
  run_with(fname,query=True)

def t13():
  fname='examples/heli'
  run_with(fname,query=True)

def t14():
  fname='examples/covid'
  run_with(fname,query=True)

def t15():
  fname='examples/wolfram'
  run_with(fname,query=True)

def t15a():
  fname='examples/wolfram'
  run_with(fname,query=True)

def t16():
  fname='examples/toxi'
  run_with(fname,query=True)

def t16a():
  fname='examples/toxi'
  run_with(fname,query=True)


def t17():
  fname = 'examples/peirce'
  run_with(fname, query=True)


def t17a():
  fname = 'examples/peirce'
  run_with(fname, query=True)

def t17b():
  fname = 'examples/peirce'
  nrun(fname)

def t18():
  fname = 'examples/ec2'
  run_with(fname, query=True)


def t18a():
  fname = 'examples/ec2'
  run_with(fname, query=True)

def t18b():
  fname = 'examples/ec2'
  nrun(fname)

def t19():
  fname = 'examples/relativity'
  run_with(fname, query=True)

def t20():
  fname = 'examples/alice'
  run_with(fname, query=True)

def api_test() :
  '''
  to be used on the server side to expose this as a web or Alexa service
  '''
  params=new_params(from_json='{"top_sum":3,"top_keys":6,"top_answers":3}')
  jsonish='''["
    The cat sits on the mat. 
    The mat sits on the floor.
    The floor sits on planet Earth.
    The Earth does not sit.
    The Earth just wanders.
  "]
  '''
  from_json=jsonish.replace('\n',' ')

  talker=new_talker(from_json=from_json,params=params)
  wss=json.loads(talker.summary_sentences())
  ks=json.loads(talker.keyphrases())

  print('SUMMARY')
  for ws in wss:
    print(" ".join(ws))

  print('KEYPHRASES')
  for k in ks:
    print(k)
  print('')
  q='Where is the mat?'
  print(q)
  r=answer_question(talker,q)
  wss=json.loads(r)

  for ws in wss :
    print(' '.join(ws))


if __name__== "__main__" :
  #ttest2()
  #t1()
  #tftest()
  #otest()
  t0()
  #otest()
  #api_test()
  #clean_text_file('examples/peirce.txt')
  #bot_test()
  #run_server()
  pass




