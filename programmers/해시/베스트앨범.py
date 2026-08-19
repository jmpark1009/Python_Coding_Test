# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 해시/베스트앨범

## '많이 재생된 장르' > '장르 내에서 많이 재생된 노래' > '고유번호가 늦은 노래'
## return은 노래의 고유 번호

### 1) 딕셔너리 2개 구축:
###    > genre_play: 장르별 총 재생 횟수 누적 (인기 장르 선정용)
###    > genre_song: 장르별 [고유번호(i), 재생횟수(play)] 튜플 리스트 수집
### 2) 장르 정렬:
###    > 총 재생 횟수(genre_play의 value) 기준 내림차순 정렬
### 3) 곡 정렬 및 베스트 앨범 수록:
###    > 인기 장르 순서대로 순회하며, 각 장르 내부 곡들을 재생 횟수 기준 내림차순 정렬
###    > 슬라이싱([:2])으로 장르당 최대 2곡의 고유 번호만 answer에 추가
def solution(genres, plays):
    genre_play = {}
    genre_song = {}
    answer = []

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre in genre_play:
            genre_play[genre] += play
        else:
            genre_play[genre] = play
        
        if genre in genre_song:
            genre_song[genre].append((i, play))
        else:
            genre_song[genre] = [(i, play)]
    
    sort_gp = sorted(genre_play.keys(),
                    key = lambda g: genre_play[g],
                    reverse = True)
    
    for genre in sort_gp:
        sort_gs = sorted(genre_song[genre],
                        key = lambda x: x[1],
                        reverse = True)

        for song in sort_gs[:2]:
                answer.append(song[0])
            
    return answer
