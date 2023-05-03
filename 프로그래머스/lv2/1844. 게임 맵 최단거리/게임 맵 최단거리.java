import java.util.LinkedList;
import java.util.Queue;

class Point{
    public int x,y;
    Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}

class Solution {
    public int BFS(int[][] maps, int x, int y) {
        int xLength = maps.length;
        int yLength = maps[0].length;
        boolean visited = false;
        
        Queue<Point> q = new LinkedList<>(); 
        q.offer(new Point(x,y));
        while(!q.isEmpty()){
            Point cur = q.poll();
            if(cur.x == xLength - 1 && cur.y == yLength-1){
                visited = true;
            }
            for(int i=0; i<4; i++){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if(0<= nx && nx < xLength && 0<= ny && ny < yLength && maps[nx][ny] == 1){
                    maps[nx][ny] = maps[cur.x][cur.y] + 1;
                    q.offer(new Point(nx,ny));
                }
            }
        }
        
        if(visited){
            return maps[maps.length-1][maps[0].length-1];
        }
        else{
            return -1;
        }
        
    }
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    
    
    public int solution(int[][] maps) {
        int answer = BFS(maps, 0, 0);
        return answer;
    }
}