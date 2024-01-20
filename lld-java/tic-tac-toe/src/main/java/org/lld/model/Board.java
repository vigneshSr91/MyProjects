package org.lld.model;

import java.util.ArrayList;
import java.util.List;

public class Board {
    private int size;
    private List<List<Cell>> board;
    public Board(int size){
        this.size = size;
        this.board = new ArrayList<>();
        for(int i=0; i<size; i++){
            board.add(new ArrayList<>());
            for (int j=0; j<size; j++){
                board.get(i).add(new Cell(i, j));
            }
        }
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public List<List<Cell>> getBoard() {
        return board;
    }

    public void setBoard(List<List<Cell>> board) {
        this.board = board;
    }

    public void print(){
        for(List<Cell> row: this.board){
            System.out.printf("| ");
            for(Cell cell: row){
                if(cell.getCellState().equals(CellState.EMPTY)){
                    System.out.printf("- | ");
                }else{
                    System.out.printf(cell.getPlayer().getSymbol().getaChar() + " | ");
                }
            }
            System.out.println();
        }
    }
}
