__author__ = 'Qiyuan Qiu, Jeffery White'

from graphlab import SFrame
from graphlab import SArray
import graphlab as gl
import json
import helper


def create_frame_from_file(file_name):
    n_total_lines = 220000
    sf = SFrame()
    with open(file_name) as data:
        dt = []
        ip = []
        py = []
        script = []
        id = []
        for i, line in enumerate(data):
            jo = json.loads(line)
            dt += jo['dt']
            ip += jo['ip']
            py += jo['py']
            id += [i]
            script += jo['user_script']

            if i % 100 == 0:
                print float(i) / n_total_lines

        sf = sf.add_column(SArray(id), name='id')
        sf.add_column(SArray(dt), name='dt')
        sf.add_column(SArray(ip), name='ip')
        sf.add_column(SArray(py, dtype=str), name='py')
        sf.add_column(SArray(script), name='user_script')

        sf.save('python_tutor')
    return sf

"""
command used to acquire the frame to be sliced
t=py3.groupby('ip',{'id':agg.CONCAT('dt','id'),'user_script':agg.CONCAT('dt','user_script'), \
'compile_err':agg.CONCAT('dt','compile_err'),'err_msg':agg.CONCAT('dt','err_msg'), 'dt':agg.CONCAT('dt')})
"""

"""
create new session sframe from sf

Columns:
	ip	str
	compile_err	dict
	count	int
	err_msg	dict
	dt	list
	id	dict
	user_script	dict
"""


def set_of_interest_bit(l):
    assert(type(l) == list)
    rst = []
    for e in l:
        assert(type(e) == dict)
        if sum(e.values()) > 0:
            rst.append(1)
        else:
            rst.append(0)
    return rst


def create_sessions(sf=SFrame()):
    assert(type(sf) == SFrame)
    ip = []
    user_script = []
    err_msg = []
    compile_err = []
    of_interest = []
    ignored = 0

    for i in xrange(len(sf)):
        count = sf['count'][i]
        if count != len(sf['id'][i]):
            ignored += 1
            continue

        tip = sf['ip'][i]
        chunk_user_script = cut_dict_by_dt(sf['user_script'][i])
        user_script += chunk_user_script
        ip += [tip,] * len(chunk_user_script)

        err_msg += cut_dict_by_dt(sf['err_msg'][i])

        chunk_compile_err = cut_dict_by_dt(sf['compile_err'][i])
        compile_err += chunk_compile_err

        of_interest += set_of_interest_bit(chunk_compile_err)

    print "DEBUG:", "ignored:", ignored
    rst = SFrame()
    rst.add_column(SArray(ip, dtype=str), name='ip')
    rst.add_column(SArray(user_script, dtype=dict), name='user_script')
    rst.add_column(SArray(err_msg, dtype=dict), name='err_msg')
    rst.add_column(SArray(compile_err, dtype=dict), name='compile_err')
    rst.add_column(SArray(of_interest, dtype=int), name='of_interest')

    return rst


def cut_dict_by_dt(d, delta="00:30:00"):
    assert(type(d) == dict)
    rst = []
    keys = sorted(d.keys())
    if len(d) <= 1:
        rst.append(d)
        return rst

    time_delta = helper.datetime_from_delta(delta)

    cnt_d = {}
    for i, k in enumerate(keys):
        try:
            cnt_dt = helper.make_datetime_struct(keys[i])
            nxt_dt = helper.make_datetime_struct(keys[i+1])
            dist = nxt_dt - cnt_dt
            cnt_d[k] = d[k]
            if dist > time_delta:
                rst.append(cnt_d)
                cnt_d = {}
        except IndexError:
            cnt_d[k] = d[k]
            assert(type(cnt_d) == dict)
            rst.append(cnt_d)

    return rst


def main():
    #sf = create_frame_from_file('../../Data/data_file_modified.txt')
    x = gl.load_sframe('py2_ready_for_session')
    sessions = create_sessions(x)
    sessions.save('session')



if __name__ == '__main__':
    main()
