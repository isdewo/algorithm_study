#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <list>
using namespace std;

void dfs(list<int> graph[], int start, bool visited[]);
void bfs(list<int> graph[], int start, bool visited[]);

int main(){
    int n, m, v;
    scanf("%d %d %d", &n, &m, &v);

    list<int> graph[n+1];

    bool visited[n+1];
    fill(visited, visited+n+1, false);

    for(int i = 0; i < m; i++){
        int x, y;
        scanf("%d %d", &x, &y);
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    for(int i = 0; i <= n; i++){
        // 내림차순 정렬 - 뒤에부터 방문 예정
        //sort(graph[i].begin(), graph[i].end(), greater<int>());

        // 오름차순 정렬
        graph[i].sort();
        //sort(graph[i].begin(), graph[i].end());
    }
  
    
    dfs(graph, v, visited);
    fill(visited, visited+n+1, false);
    printf("\n");
    bfs(graph, v, visited);
    
}

void dfs(list<int> graph[], int start, bool visited[]){
    // 시작점 방문
    visited[start] = true;
    printf("%d ", start);

/*
    // 인접노드 찾아서 방문
    while(graph[start].empty() != true){
        int search = graph[start].back();
        if(visited[search] == false){
            dfs(graph, search, visited);
        }
        graph[start].pop_back();

    }
*/
    for(int i = 0; i < graph[start].size(); i++){
        int search = graph[start].front();
        graph[start].pop_front();
        if (visited[search] == false){
            dfs(graph, search, visited);
        }
        graph[start].push_back(search);
    }
    
}

void bfs(list<int> graph[], int start, bool visited[]){
/*    
    list<int>queue;
    visited[start] = true;
    queue.push_back(start);
    printf("%d ", start);

    for(int i = 0; queue.empty() == false; i++){
        int search = queue.front();
        if(visited[search] == false){
            printf("%d ", search);
            for(int j = 0; j < graph[i].size(); j++){
                queue.push_back(graph[search][j]);
            }
        }
        queue.pop_front();
    }
*/
    list<int>queue;
    queue.push_back(start);

    for(int i = 0; queue.empty() == false; i++){
        int search = queue.front();
        if(visited[search] == false){
            printf("%d ", search);
            visited[search] = true;
            int size = graph[search].size();
            for(int j = 0; j < size; j++){
                queue.push_back(graph[search].front());
                graph[search].pop_front();
            }
        }
        queue.pop_front();
    }
  printf("\n");  
}
