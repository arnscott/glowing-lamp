import networkx as nx

import lib.parser




def split_reads_into_mers(read, kmer_size):
    kmer_list = []
    for i in range((len(read) - (kmer_size - 1))):
        kmer = read[i:i+kmer_size]
        kmer_list.append(kmer)
    return kmer_list



def compare(sequence_1, sequence_2, n):
    seq_1_length = len(sequence_1) - 1
    seq_2_length = len(sequence_2) - 1
    seq_1_slice = sequence_1[-(n - 1):]
    seq_2_slice = sequence_2[:n - 1]
    if seq_1_slice == seq_2_slice:
        return seq_1_length, True
    return 0, False


def make_simplified_string(graph, start_node, n):
    simple_string = start_node
    still_nodes = True
    node = start_node
    used_nodes.append(node)
    while still_nodes:
        successors = [succ for succ in graph.successors(node)]
        if not successors:
            still_nodes = False
        elif len(successors) > 1:
            still_nodes = False
        else:
            simple_string = simple_string + successors[0][n-1:]
            node = successors[0]
            used_nodes.append(node)
    return simple_string, used_nodes



def compare_for_merge(sequence_1, sequence_2, n):
    seq_1_length = len(sequence_1) - 1
    seq_2_length = len(sequence_2) - 1
    seq_1_slice = sequence_1[-(n - 1):]
    seq_2_slice = sequence_2[:n - 1]
    if seq_1_slice == seq_2_slice:
        print(seq_1_slice, seq_2_slice, sequence_1, sequence_2)
        return seq_1_length, True
    return 0, False








