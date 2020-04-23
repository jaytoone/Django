import pandas as pd
pd.set_option('display.max_columns', 1500)

#               데이터 로딩              #
absent_df = pd.read_csv('이미지분석 A반 출석현황.csv', index_col=0)
# print(absent_df.iloc[0])
# quit()

#   누적 출석 시간 / 현재까지 정상 출석 시간 = 실시간 출석률
#   현재까지 정상 출석 시간 = 1주차부터 해당 주차까지의 정상 출석 시간
#   = 40시간 * 10주차 = 400시간
#                   시간은 분 단위로 계산한다                  #


def total_min(str_time):
    hour = str_time.split(':')[0]
    min = str_time.split(':')[1]
    return int(hour) * 60 + int(min)


column_lines = absent_df.iloc[:1]
data_lines = absent_df.iloc[1:]
# print(column_lines)
# quit()


name = input('이름을 입력하세요 : ')
print()
selected_line = data_lines[data_lines['이름'] == name]
number = int(selected_line.index[0])
# print(number)
# quit()

import re

# week_number = column_lines[column_lines.columns[6]].iloc[0].split()[0]
# week_number = int(re.findall('\d+', week_number)[0])
# 총 출석일 수
# total_attendance = (len(selected_line.columns) - 6) * 8 * 60
total_attendance = (50) * 8 * 60
stacked_attendance = selected_line[selected_line.columns[-4]].values[0]
realtime_attendance = total_min(stacked_attendance) / total_attendance
print('### 실시간 출석률 : %.2f %% ###' % (realtime_attendance * 100))

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
# print(selected_line)
print()

#   일별 출석률


#   특이사항
print('### 특이사항 ###')
print(selected_line[selected_line.columns[-2]].values)
    
#     except Exception as e:
#         print('Error occured :', e)