/*
    완주하지 못한 선수
    레벨 1
    해쉬
*/

/* participant : 참여한 선수 이름이 담긴 배열, completion : 완주한 선수 이름이 담긴 배열 */
/* return : 완주하지 못한 선수 */
function solution(participant, completion) {
    const result = participant.filter(person => {
        if (completion.indexOf(person) === -1) {
            participant.
        }
        return completion.indexOf(person) === -1
    })
    return result[0];
}

const participant = ["mislav", "stanko", "mislav", "ana"]
const completion = ["stanko", "ana", "mislav"]

solution(participant, completion)