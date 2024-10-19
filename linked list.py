class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __str__(self):
        return str(self.value)


class List:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.size = 0

    def _perc(self, index):
        half = (self.size//2)
        if index <= half:
            corredor = self.head
            for i in range(index):
                corredor = corredor.next
        else:
            corredor = self.tail
            meio = self.size - (index)
            for h in range(meio):
                corredor = corredor.previous
        return corredor

    def __str__(self):
        colcht1 = "["
        perc = self.head

      
        while perc is not None:
            if perc.next is not None:
                colcht1 += f'{perc.value}, '
            else:
                colcht1 += f'{perc.value}'
            perc = perc.next
        colcht1 += "]"
        return colcht1
        

    def __len__(self):
        return self.size 

    def add(self, value):
        noh = Node(value)
        self.size += 1
        
        if self.head is None:
            self.head = noh
            self.tail = noh 
            return
        
        self.tail.next = noh
        noh.previous = self.tail
        self.tail = noh 
        
    def insert(self, index, value):
        if self.size == 0 or index >= self.size:
            self.add(value)
        
        noh = Node(value) #cria novo nó

        percorre = self._perc(index - 1) #pega o nó anterior ao index

        noh.next = percorre.next #aponta noh.next = para o noh que estava naquele indice      
        noh.previous = percorre #aponta noh.previous para no anterior
        noh.next.previous = noh #aponta o anterior do index para o novo noh
        percorre.next = noh #aponta o noh anterior ao index para o novo noh naquela posiçao


    def remove_index(self, index):
        if self.size == 0 or index >= self.size:
            raise Exception("Index não existente")
        
        self.size -= 1
        
        if index == 0:
            atual = self.head
            self.head = atual.next
            if self.head is not None: 
                self.head.previous = None
            else: 
                self.tail = None
            return atual
        else:
            corredor = self._perc(index - 1)
            atual = corredor.next
            corredor.next = atual.next
            if atual.next is not None: 
                atual.next.previous = corredor
            else: 
                self.tail = corredor
            return atual
             
    def remove_value(self, value):
        atual = self.head
        index = 0
        while atual:
            if atual.value == value:
                self.remove_index(index)  # Remove o nó com base no índice
                return True  # Valor encontrado e removido, então retorne True
            atual = atual.next
            index += 1

        raise ValueError("Valor não encontrado na lista")  # Se o valor não foi encontrado
            

    def get_index(self, value):
        i = 0
        atual = self.head
        while i < self.size:
            if value == atual.value:
                return i
            atual = atual.next
            i += 1
        else:
            if atual == self.tail:
                return i
        raise Exception("Valor não encontrado")

    def invert_index(self, index_a, index_b):
        if index_a == index_b:
            return 
        if index_a < 0 or index_b < 0 or index_b >= self.size or index_a >= self.size:
            raise IndexError("Index fora da range")
        noh_a = self._perc(index_a)
        noh_b = self._perc(index_b)

        noh_a.value,noh_b.value = noh_b.value, noh_a.value

    def invert(self):
        perc = self.tail
        result = "["
        while perc.previous is not None:
            result += f'{str(perc.value)},'
            perc = perc.previous    
        else:
            result += f'{perc.value}'
        result += "]"
        return result

    def set_value(self, index, value):
        try:
            search_index = self._perc(index)
            search_index.value = value
        except:
            raise("Index não encontrado")
        
        
    def impar_par(self):
        perc = self.head
        while perc is not None and perc.next is not None:
            valor_atual = perc.value
            valor_proximo = perc.next.value
            
            perc.value = valor_proximo
            perc.next.value = valor_atual
            
            # Avançar para o próximo par
            perc = perc.next.next


    def sum(self):
        total = 0
        perc = self.head
        while perc is not None:
            total += perc.value
            perc = perc.next

        return total

    def sum_index_par(self):
        total = 0
        index = 0 
        perc = self.head 

        while perc is not None:
            if index % 2 == 0:
                total += perc.value
            perc = perc.next
            index += 1
        return total

    def sum_index_impar(self):
        
        total = 0
        index = 0 
        perc = self.head 

        while perc is not None:
            if index % 2 == 1:
                total += perc.value
            perc = perc.next
            index += 1
        return total


    def clear(self):
        atual = self.head
        while atual is not None:
            proximo = atual.next
            atual.previous = None
            atual.next = None
            atual = proximo
        
        self.head = None
        self.tail = None
        self.size = 0

        return None
    def contains(self, value):
        perc = self.head
        while perc is not None:
           if perc.value == value:
               return True
           perc = perc.next
        else:
            return False
           

    def count(self, value):
        total = 0
        perc = self.head
        while perc is not None:
            if perc.value == value:
                total += 1
            perc = perc.next
            if total == 0:
                return "Valor não encontrado"
        return total   
    

    def slice(self, start, end):  
        if start < 0 or end > self.size or start >= end:
            raise IndexError("Índice fora do inválido")

        colcht1 = "["
        inicio = self._perc(start)

        for _ in range(end - start):
            colcht1 += f'{inicio.value}, '
            inicio = inicio.next
        
        colcht1 = colcht1.rstrip(', ') 
        colcht1 += "]"

        return colcht1

    def merge(self, other_list): 

        if other_list.head is None:  
            return
        
        if self.head is None:  # caso a outra lista esteja vazia
            self.head = other_list.head
            self.tail = other_list.tail
        else: # conecte as listas
            self.tail.next = other_list.head
            other_list.head.previous = self.tail
            self.tail = other_list.tail
        
        self.size += other_list.size


    def reverse(self):
        atual = self.head
        prev_head = self.head  # Armazena o antigo head para se tornar o novo tail
        while atual is not None:
            atual.next, atual.previous = atual.previous, atual.next
            atual = atual.previous
        
        # Após a inversão, troque head e tail
        self.head, self.tail = self.tail, prev_head

    def find_middle(self):
        if self.head is None:
            return None  # Retorna None se a lista estiver vazia

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.value


