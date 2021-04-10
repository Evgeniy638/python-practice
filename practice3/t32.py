class C32:
    def __init__(self):
        self.current_vertex = 'A'
        self.arcs_log = [
            {
                'start': 'A',
                'end': 'B',
                'result': 0
            },
            {
                'start': 'C',
                'end': 'D',
                'result': 2
            },
            {
                'start': 'E',
                'end': 'F',
                'result': 5
            },
            {
                'start': 'F',
                'end': 'F',
                'result': 7
            },
            {
                'start': 'G',
                'end': 'D',
                'result': 9
            }
        ]
        self.arcs_amble = [
            {
                'start': 'B',
                'end': 'C',
                'result': 1
            },
            {
                'start': 'C',
                'end': 'E',
                'result': 3
            },
            {
                'start': 'D',
                'end': 'E',
                'result': 4
            },
            {
                'start': 'F',
                'end': 'G',
                'result': 6
            },
            {
                'start': 'G',
                'end': 'G',
                'result': 8
            }
        ]
    
    def log(self):
        find_arcs = [arc for i, arc in enumerate(self.arcs_log) if arc["start"] == self.current_vertex]

        if len(find_arcs) == 0:
            raise RuntimeError

        arc = find_arcs[0]
        self.current_vertex = arc["end"]
        return arc["result"]
    
    def amble(self):
        find_arcs = [arc for i, arc in enumerate(self.arcs_amble) if arc["start"] == self.current_vertex]

        if len(find_arcs) == 0:
            raise RuntimeError

        arc = find_arcs[0]
        self.current_vertex = arc["end"]
        return arc["result"]
