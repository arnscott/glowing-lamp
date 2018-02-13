

class FASTQRecord(object):

    def __init__(self, id_line, sequence, quality_line):
        self.raw_id_line = id_line
        self.sequence = sequence
        self.quality_line = quality_line

    @property
    def id_line(self):
        return self.raw_id_line.replace('@', '')




class FASTQFile(object):

    def __init__(self, file_path):
        self.file_path = file_path
        return

    @property
    def iterate(self):
        with open(self.file_path) as fastq_file:
            id_line = ''
            sequence = ''
            quality_line = ''
            for line in fastq_file:
                if line.startswith('@'):
                    id_line = line.strip('\n')
                    sequence_line = next(fastq_file)
                    sequence = sequence_line.strip('\n')
                elif line.startswith('+'):
                    scoring_line = next(fastq_file)
                    scoring = scoring_line.strip('\n')
                    yield FASTQRecord(id_line=id_line,
                                      sequence=sequence,
                                      quality_line=quality_line)
                    id_line = ''
                    sequence = ''
                    scoring = ''





class FASTARecord(object):

    def __init__(self, id_line='', sequence=''):
        self.id_line = id_line.strip('\n')
        self.sequence = sequence.strip('\n')


    @property
    def info_line(self):
        split_line = self.id_line.split('\t')
        return split_line[0].replace('>', '')



class FASTAFile(object):

    def __init__(self, file_location):
        self.file_location = file_location
        return

    @property
    def iterate(self):
        with open(self.file_location) as fasta_file:
            info_line = ''
            sequence = ''
            end_of_sequence = False
            for line in fasta_file:
                if line.startswith('>'):
                    if sequence:
                        end_of_sequence = True
                    if end_of_sequence:
                        yield FASTARecord(id_line=info_line,
                                          sequence=sequence)
                        info_line = line
                        sequence = ''
                    else:
                        info_line = line
                else:
                    sequence += line.strip('\n')
            if sequence:
                yield FASTARecord(id_line=info_line,
                                  sequence=sequence)
                sequence = ''
                info_line = ''

