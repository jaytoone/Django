import pandas as pd
import re

pd.set_option('display.max_columns', 1500)

#               데이터 로딩              #
# print(absent_df.iloc[0])
# quit()

def total_min(str_time):
    hour = str_time.split(':')[0]
    min = str_time.split(':')[1]
    return int(hour) * 60 + int(min)

def absent_check(name):

    absent_df = pd.read_csv('dataset/이미지분석 A반 출석현황.csv', index_col=0)
    column_lines = absent_df.iloc[:1]
    data_lines = absent_df.iloc[1:]
    # print(column_lines)
    # quit()

    #       index html 로 부터 이름을 입력받는다       #
    # name = input('이름을 입력하세요 : ')
    print()
    selected_line = data_lines[data_lines['이름'] == name]
    number = int(selected_line.index[0])
    # print(number)
    # quit()


    #   누적 출석 시간 / 현재까지 정상 출석 시간 = 실시간 출석률
    #   현재까지 정상 출석 시간 = 1주차부터 해당 주차까지의 정상 출석 시간
    #   = 40시간 * 10주차 = 400시간
    #                   시간은 분 단위로 계산한다                  #
    # week_number = column_lines[column_lines.columns[6]].iloc[0].split()[0]
    # week_number = int(re.findall('\d+', week_number)[0])
    # 총 출석일 수
    # total_attendance = (len(selected_line.columns) - 6) * 8 * 60
    total_attendance = (50) * 8 * 60
    stacked_attendance = selected_line[selected_line.columns[-4]].values[0]
    realtime_attendance = total_min(stacked_attendance) / total_attendance * 100
    print('### 실시간 출석률 : %.2f %% ###' % (realtime_attendance))

    #   출결 석차 = 누적 출석률 내림차순 정렬
    #   누적 출석률 column 추출
    data_lines[data_lines.columns[-4]] = data_lines[data_lines.columns[-4]].apply(total_min)
    Rank_lines = data_lines.sort_values(by=[data_lines.columns[-4]], ascending=False).reset_index(drop=True)
    Rank = Rank_lines[Rank_lines['이름'] == name].index[0] + 1
    print('### %s명 중 %s등 ###' % (len(Rank_lines), Rank))

    #   퇴소까지 남은 결석 시간 = 184시간 - 총 결석 시간
    absent_time = selected_line[selected_line.columns[-1]].values[0]
    rest_time = (184 * 60 - total_min(absent_time)) / 60
    rest_day = rest_time / 8
    print('### 퇴소까지 %.2f일 (%.2f시간) 남았습니다. ###' % (rest_day, rest_time))
    print()

    #   일별 출석 시간, 특이사항 조회 (데이터 베이스에서 가져오기)
    print('### 일별 출석 시간 ###')
#     print(selected_line[selected_line.index == '월'])
    #     해당 요일을 모으기    #
    yo_il_dict = {'mon':'월', 'tue':'화', 'wed':'수', 'thur':'목', 'fri':'금'}
    daytime_attendance_dict = dict()
#     print(yo_il_dict.values())
    #     월, 토는 묶어주기    #
    for yo_il in yo_il_dict.keys():
        day_list = list()
        for column in selected_line.columns:
            if yo_il_dict[yo_il] in list(column):
                day_list.append(column)
        if yo_il_dict[yo_il] == '월':
            for column in selected_line.columns:
                if '토' in list(column):
                    day_list.append(column)
#     print(day_list)
#     quit()

        #   일별 출석률
        stacked_day_attendance = sum(list(map(total_min, list(selected_line[day_list].values[0]))))
        total_day_attendance = 8 * 60 * len(day_list)
        daytime_attendance = stacked_day_attendance / total_day_attendance
        daytime_attendance_dict[yo_il] = int(daytime_attendance * 100)
    print(daytime_attendance_dict)

    #   특이사항
    print('### 특이사항 ###')
    uniqueness = selected_line[selected_line.columns[-2]].values
    print(uniqueness)

    #    수료까지 남은 시간    #
    print('### 수료까지 남은 시간 ###')
    till_end_time = (920 * 60 * 0.8 - total_min(stacked_attendance)) / 60
    till_end_day = till_end_time / 8
    print(till_end_time, '시간')
    print(till_end_day, '일')

    # 출석률에 따른 매니저 코멘트
    comment = ''
    if 90 < realtime_attendance < 100:
        comment = "잠은......자고 나오셨나요?"
    elif 80 < realtime_attendance < 90:
        comment = "열심히 일한 당신에게 해외 여.....아니 추가 간식권을 수여합니다"
    elif 70 < realtime_attendance < 80:
        comment = "하루만.....하루만 더 나와보자"
    elif 60 < realtime_attendance < 70:
        comment =  "얼마면 나올래!! 얼마면 되냐고!!!"
    else:
        comment = "하기 싫음 하지 마라"

    phrase = [

    ('당신의 진정한 모습은 당신이 반복적으로 행하는 행위의 축적물이다. 탁월함은 하나의 사건이 아니라 습성인 것이다.' ,'"We are what we repeatedly do. Excellence, then, is not an act, but a habit."', '아리스토텔레스(Aristotle)'),
    ('한 걸음 한 걸음 단계를 밟아 나아가라. 그것이 무언가를 성취하기 위한 내가 아는 유일한 방법이다.' ,'"Step by step. I cant see any other way of accomplishing anything."','마이클 조던(Michael jordan)'),
     ('끊임 없이 노력하라. 체력이나 지능이 아니라 노력이야 말로 잠재력의 자물쇠를 푸는 열쇠다.','“Continuous effort — not strength or intelligence — is the key to unlocking our potential.”','윈스턴 처칠(Winston Churchill)'),
    ('노력이 지겨워질 때조차 한 걸음 더 나아가도록 자신을 독려할 수 있는 사람이 승리를 거머쥔다.', '“The man who can drive himself further once the effort gets painful is the man who will win.”','로저 배니스터(Roger Bannister)'),
    ('당신이 할 수 있다고 생각하든 할 수 없다고 생각하든, 당신의 생각은 옳다.','"If you think you can do a thing or think you cant do a thing, youre right."' ,'헨리 포드(Henry Ford)'),
    ('눈앞의 실패에 좌절하지 않을 수 있는 장기 목표를 반드시 가지고 있어야 한다.','"You must have long term goals to keep you from being frustrated by short term failures."' ,'찰스 C 노블(Charles C Noble)')
]

    import random
    phrase = random.choice(phrase)


    return {'name':name, 'realtime_attendance':round(realtime_attendance, 2), 'Rank_lines':len(Rank_lines), 'Rank':Rank,
    'rest_day':round(rest_day, 2), 'rest_time':round(rest_time, 2), 'daytime_attendance_dict':daytime_attendance_dict,
            'uniqueness':uniqueness, 'till_end_time':round(till_end_time, 2), 'till_end_day':round(till_end_day, 2), 'comment':comment, 'phrase': phrase}



#     except Exception as e:
#         print('Error occured :', e)
