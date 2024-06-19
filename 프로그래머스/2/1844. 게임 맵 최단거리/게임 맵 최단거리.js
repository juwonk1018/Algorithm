function solution(maps) {
    var answer = 0;
    var [n,m] = [maps.length, maps[0].length];
    
    var dx = [1,0,0,-1];
    var dy = [0,1,-1,0];
    
    var distance = [];
    for(let i=0;i<n;i++){
        distance.push(new Array(m).fill(Infinity))
    }
    
    distance[0][0] = 1;
    
    var queue = [[0,0]];
    
    while(queue.length !== 0){
        
        if(distance[n-1][m-1] !== Infinity){
            return distance[n-1][m-1];
        }
        
        [cx,cy] = queue.shift()
        
        for(let i=0;i<4;i++){
            [nx,ny] = [Number(cx + dx[i]),Number(cy + dy[i])];
            
            if(0<= nx && nx<n && 0<=ny && ny<m && maps[nx][ny] === 1 && distance[cx][cy] + 1 < distance[nx][ny]){
                
                
                distance[nx][ny] = distance[cx][cy] + 1;
                queue.push([nx,ny]);
            }  
        }
    }
    
    return -1;
    
}