//
//  PieceView.swift
//  Chess
//
//  Created by Kaede Sugano on 22/12/2023.
//

import SwiftUI

struct PieceView: View {
    @GestureState private var dragOffset = CGSize.zero // Tracks the drag state
    @ObservedObject var viewModel: ChessboardViewModel
    @State private var position: CGPoint

    var piece: ChessPiece
    var onButtonTap: (ChessPiece) -> Void
    let cellWidth = (screenWidth * 0.78) / CGFloat(columns)
    let cellHeight = (screenWidth * 0.75) / CGFloat(columns)
    
    init(side: ChessSide, row: Int, column: Int, viewModel: ChessboardViewModel, onButtonTap: @escaping (ChessPiece) -> Void) {
        let initialPosition = ChessboardHelper.positionForRowAndColumn(row: row, column: column, cellWidth: cellWidth, cellHeight: cellHeight)
        self._position = State(initialValue: initialPosition)
        self.viewModel = viewModel
        self.piece = ChessPiece(name: viewModel.pieces[row][column].name, side: side, row: row, column: column)
        self.onButtonTap = onButtonTap
    }
    
    var body: some View {
        let imgName = convertPieceNametoImg(name: piece.name)
        if (imgName != "") {
            ZStack {
                Image(imgName) // Replace with your chess piece image
                    .resizable()
                    .scaledToFit()
                    .frame(width: dragOffset.width == 0 ? cellWidth : cellWidth * 1.5, height: dragOffset.height == 0 ? cellHeight : cellHeight * 1.5)
                    .position(x: position.x + dragOffset.width, y: position.y + dragOffset.height) // Update position during drag
                    .gesture(
                        DragGesture()
                            .updating($dragOffset, body: { (value, state, transaction) in
                                state = value.translation
                            })
                            .onEnded { value in
                                handleDragEnd(value: value)
                            }
                    )
                    .onTapGesture {
                        self.onButtonTap(piece)
                    }
            }
        }
    }
    
    private func handleDragEnd(value: DragGesture.Value) {
        // Calculate the new position based on the drag offset
        let horizontalCellsMoved = Int(round(value.translation.width / cellWidth))
        let verticalCellsMoved = Int(round(value.translation.height / cellHeight))
        
        let newColumn = piece.column + horizontalCellsMoved
        let newRow = piece.row + verticalCellsMoved
        
        // Check if the move is valid and within bounds
        if isValidMove(toRow: newRow, toColumn: newColumn) {
            viewModel.movePiece(fromRow: piece.row, fromColumn: piece.column, toRow: newRow, toColumn: newColumn)
        }
    }
    
    private func isValidMove(toRow: Int, toColumn: Int) -> Bool {
        // TODO: Add logic here to validate the move
        return true
    }
    
    private func convertPieceNametoImg(name: String) -> String {
        let sideStr: String = piece.side == .black ? "b_" : "w_"
        switch name {
        case "p":
            return sideStr+"pawn"
        case "k":
            return sideStr+"king"
        case "q":
            return sideStr+"queen"
        case "n":
            return sideStr+"knight"
        case "b":
            return sideStr+"bishop"
        case "r":
            return sideStr+"rook"
        default:
            return ""
        }
    }
}
