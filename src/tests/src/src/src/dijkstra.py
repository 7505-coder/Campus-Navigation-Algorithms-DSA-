# src/dijkstra.py
import heapq
from graph_adjlist import edges,build_adjlist

def dijkstra(s,t):
    g=build_adjlist(edges)
    dist={i:1e18 for i in g}; parent={}
    dist[s]=0; pq=[(0,s)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]: continue
        if u==t: break
        for v,w in g[u]:
            nd=d+w
            if nd<dist[v]: dist[v]=nd; parent[v]=u; heapq.heappush(pq,(nd,v))
    if dist[t]>1e17: return None,None
    path=[]; cur=t
    while cur!=s:
        path.append(cur); cur=parent[cur]
    path.append(s); path.reverse()
    return path,dist[t]

def demo_dijkstra():
    p,d=dijkstra(1,4)
    print("Dijkstra 1->4:", p, d)
