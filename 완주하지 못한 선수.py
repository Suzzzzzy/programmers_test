participant = ["mislav", "stanko", "ana", "mislav", "mislav"]
completion = ["stanko", "ana", "mislav", "mislav"]
answer = ''
#1안 -> 효율성 실패
# for i in participant:
#     if participant.count(i) > 1 :
#         if participant.count(i) >  completion.count(i) :
#             answer = i
#     elif i not in completion :
#         answer = i 
# print(answer)

# answer = list(set(participant) - set(completion))
# print(set(participant)- set(completion))

if set(completion)== set(participant) :
    for i in participant:
        if participant.count(i) > 1 :
            answer = i
            break
else :
    answer = ''.join(list(set(participant) - set(completion)))

print(answer)

