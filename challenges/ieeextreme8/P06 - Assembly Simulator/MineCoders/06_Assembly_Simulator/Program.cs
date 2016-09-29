/*
 * Copyright (C) 2014 MineCoders
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 3
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public delegate void ProcessCommand(Command cmd);

public struct Command 
{
	public string    Label    { get; private set; }
	public string    Action   { get; private set; }
	public Operand[] Operands { get; private set; }
	public string    Id       { get; private set; }

	public static Command FromString(string str)
	{
		string[] fields = str.Split(new char[] { ' ' }, 
			StringSplitOptions.RemoveEmptyEntries);
		Command cmd = new Command();

		int idx = 0;
		cmd.Label = (fields.Length == 3) ? fields[idx++] : string.Empty;
		cmd.Action = fields[idx++];

		// Clave para reconocer unívocamente el comando
		StringBuilder id = new StringBuilder(cmd.Action);

		// Procesa los operandos
		string[] ops = fields[idx++].Split(',');
		cmd.Operands = new Operand[ops.Length];
		for (int i = 0; i < ops.Length; i++) {
			if (cmd.Action[0] == 'B') // Salto, es una label
				cmd.Operands[i] = new Operand(ops[i], OperandType.Label);
			else
				cmd.Operands[i] = Operand.FromString(ops[i]);
			id.Append(cmd.Operands[i].Type.ToString()[0]);
		}

		cmd.Id = id.ToString();
		return cmd;
	}

	public override string ToString()
	{
		return string.Format("[Command: Label={0}, Action={1}, Operands={2}, Id={3}]",
			Label, Action, Operands, Id);
	}
}

public struct Operand
{
	public string      Value { get; private set; }
	public OperandType Type  { get; private set; }
	public byte AsByte {
		get {
			return Convert.ToByte(Value, 16);
		}
	}

	public Operand(string value, OperandType type) : this()
	{
		this.Value = value;
		this.Type  = type;
	}

	/// <summary>
	/// Crea un comando a partir de un string. NO DETECTA LAS LABELS.
	/// </summary>
	/// <returns>The string</returns>
	/// <param name="op">Operand</param>
	public static Operand FromString(string op) 
	{
		if (op[0] == '#')
			return new Operand(op.Substring(1), OperandType.Constant);
		else if (op[0] == '(')
			return new Operand(op.Substring(1, op.Length - 2), OperandType.MemoryPointer);
		else
			return new Operand(op, OperandType.Pointer);
	}
}

public enum OperandType 
{
	Pointer,
	MemoryPointer,
	Constant,
	Label
}

class Solution
{
	private readonly Dictionary<string, ProcessCommand> actions;
	private Command[] commands;
	private byte[] memory;

	private int pc;
	private bool flagZ;
	private bool flagC;

	public Solution(int memSize, Command[] cmds)
	{
		this.memory   = new byte[memSize];
		this.commands = cmds;
		this.actions = new Dictionary<string, ProcessCommand>() {
			{ "PRINTP",  new ProcessCommand(PrintAddr) },
			{ "PRINTPP", new ProcessCommand(PrintRange) },
			{ "MOVECP",  new ProcessCommand(MoveConstantPointer) },
			{ "MOVECM",  new ProcessCommand(MoveConstantRef) },
			{ "MOVEMP",  new ProcessCommand(MoveRefPointer) },
			{ "MOVEMM",  new ProcessCommand(MoveRefRef) },
			{ "MOVEPM",  new ProcessCommand(MovePointerRef) },
			{ "MOVEPP",  new ProcessCommand(MovePointerPointer) },
			{ "ADDCP",   new ProcessCommand(AddConstantPointer) },
			{ "ADDPP",   new ProcessCommand(AddPointerPointer) },
			{ "SUBCP",   new ProcessCommand(SubConstantPointer) },
			{ "SUBPP",   new ProcessCommand(SubPointerPointer) },
			{ "ANDCP",   new ProcessCommand(AndConstantPointer) },
			{ "ANDPP",   new ProcessCommand(AndPointerPointer) },
			{ "ORCP",    new ProcessCommand(OrConstantPointer) },
			{ "ORPP",    new ProcessCommand(OrPointerPointer) },
			{ "XORCP",   new ProcessCommand(XorConstantPointer) },
			{ "XORPP",   new ProcessCommand(XorPointerPointer) },
			{ "COMPCP",  new ProcessCommand(CompareConstantPointer) },
			{ "COMPPP",  new ProcessCommand(ComparePointerPointer) },
			{ "BEQL",    new ProcessCommand(BranchEq) },
			{ "BNEL",    new ProcessCommand(BranchNotEq) },
			{ "BGTL",    new ProcessCommand(BranchGreaterThan) },
			{ "BLTL",    new ProcessCommand(BranchLessThan) },
			{ "BGEL",    new ProcessCommand(BranchGreaterEqThan) },
			{ "BLEL",    new ProcessCommand(BranchLessEqThan) }
		};
	}

	public static void Main (string[] args)
	{
		// Lee el tamaño de la memoria
		int memSize = Convert.ToInt32(Console.ReadLine(), 16) + 1;

		// Lee los comandos
		List<Command> cmds = new List<Command>();
		string line = Console.ReadLine();
		while (line != null) {
			// Lee el comando
			cmds.Add(Command.FromString(line));

			// Lee la siguiente línea
			line = Console.ReadLine();
		}

		// Crea el simulador y comienza
		Solution simulador = new Solution(memSize, cmds.ToArray());
		simulador.Run();
	}

	public void Run() 
	{
		this.pc = 0;
		while (this.pc < this.commands.Length) {
			// Obtiene el comando y avanza PC
			Command cmd = this.commands[this.pc++];

			// Invoca al comando
			this.actions[cmd.Id].Invoke(cmd);
		}
	}

	#region Operaciones
	private void PrintAddr(Command cmd) {
		byte addr = Convert.ToByte(cmd.Operands[0].Value, 16);
		Console.WriteLine(this.memory[addr].ToString("X2"));
	}

	private void PrintRange(Command cmd) {
		byte start = Convert.ToByte(cmd.Operands[0].Value, 16);
		byte end = Convert.ToByte(cmd.Operands[1].Value, 16);

		for (int i = start; i <= end; i++) {
			Console.Write(this.memory[i].ToString("X2"));
			if (i != end)
				Console.Write(" ");
		}

		Console.WriteLine();
	}

	private void MoveConstantPointer(Command cmd) {
		byte value = Convert.ToByte(cmd.Operands[0].Value, 16);
		byte addr  = Convert.ToByte(cmd.Operands[1].Value, 16);
		this.memory[addr] = value;
	}

	private void MoveConstantRef(Command cmd) {
		byte value = Convert.ToByte(cmd.Operands[0].Value, 16);
		byte point = Convert.ToByte(cmd.Operands[1].Value, 16);
		byte addr  = this.memory[point];
		this.memory[addr] = value;
	}

	private void MoveRefPointer(Command cmd) {
		byte point = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		byte addrSrc = this.memory[point];
		this.memory[addrDst] = this.memory[addrSrc];
	}

	private void MoveRefRef(Command cmd) {
		byte pointSrc = cmd.Operands[0].AsByte;
		byte pointDst = cmd.Operands[1].AsByte;

		byte addrSrc = this.memory[pointSrc];
		byte addrDst = this.memory[pointDst];

		this.memory[addrDst] = this.memory[addrSrc];
	}

	private void MovePointerRef(Command cmd) {
		byte addrSrc = cmd.Operands[0].AsByte;
		byte pointDst = cmd.Operands[1].AsByte;

		byte addrDst = this.memory[pointDst];
		this.memory[addrDst] = this.memory[addrSrc];
	}

	private void MovePointerPointer(Command cmd) {
		byte src = Convert.ToByte(cmd.Operands[0].Value, 16);
		byte dst = Convert.ToByte(cmd.Operands[1].Value, 16);
		this.memory[dst] = this.memory[src];
	}

	private void AddConstantPointer(Command cmd) {
		byte value = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] += value;
	}

	private void AddPointerPointer(Command cmd) {
		byte addr1 = Convert.ToByte(cmd.Operands[0].Value, 16);
		byte addr2 = Convert.ToByte(cmd.Operands[1].Value, 16);

		this.memory[addr2] += this.memory[addr1];
	}

	private void SubConstantPointer(Command cmd) {
		byte value = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] -= value;
	}

	private void SubPointerPointer(Command cmd) {
		byte addrSrc = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] -= this.memory[addrSrc];
	}

	private void AndConstantPointer(Command cmd) {
		byte value = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] &= value;
	}

	private void AndPointerPointer(Command cmd) {
		byte addrSrc = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] &= this.memory[addrSrc];
	}

	private void OrConstantPointer(Command cmd) {
		byte value = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] |= value;
	}

	private void OrPointerPointer(Command cmd) 
	{
		byte addrSrc = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] |= this.memory[addrSrc];
	}

	private void XorConstantPointer(Command cmd)
	{
		byte value   = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] ^= value;
	}

	private void XorPointerPointer(Command cmd)
	{
		byte addrSrc = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.memory[addrDst] ^= this.memory[addrSrc];
	}

	private void CompareConstantPointer(Command cmd)
	{
		byte value   = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.flagZ = (value == this.memory[addrDst]);
		this.flagC = (value > this.memory[addrDst]);
	}

	private void ComparePointerPointer(Command cmd)
	{
		byte addrSrc = cmd.Operands[0].AsByte;
		byte addrDst = cmd.Operands[1].AsByte;

		this.flagZ = (this.memory[addrSrc] == this.memory[addrDst]);
		this.flagC = (this.memory[addrSrc] > this.memory[addrDst]);
	}

	private void BranchEq(Command cmd)
	{
		if (this.flagZ)
			this.pc = this.SearchCommandLabel(cmd.Operands[0].Value);
	}

	private void BranchNotEq(Command cmd)
	{
		if (!this.flagZ)
			this.pc = this.SearchCommandLabel(cmd.Operands[0].Value);
	}

	private void BranchGreaterThan(Command cmd)
	{
		if (this.flagC && !this.flagZ)
			this.pc = this.SearchCommandLabel(cmd.Operands[0].Value);
	}

	private void BranchLessThan(Command cmd)
	{
		if (!this.flagC && !this.flagZ)
			this.pc = this.SearchCommandLabel(cmd.Operands[0].Value);
	}

	private void BranchGreaterEqThan(Command cmd)
	{
		if (this.flagC || this.flagZ)
			this.pc = this.SearchCommandLabel(cmd.Operands[0].Value);
	}

	private void BranchLessEqThan(Command cmd)
	{
		if (!this.flagC || this.flagZ)
			this.pc = this.SearchCommandLabel(cmd.Operands[0].Value);
	}

	private int SearchCommandLabel(string label)
	{
		for (int i = 0; i < this.commands.Length; i++)
			if (this.commands[i].Label == label)
				return i;

		return -1;
	}

	#endregion
}
